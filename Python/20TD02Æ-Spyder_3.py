python
import subprocess
import paramiko
import logging
import getpass

# Konfigurasjon
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- WINDOWS SERVER FUNKSJONER ---
def run_powershell_command(command, elevated=False):
    """Kjører en PowerShell-kommando, valgfritt med forhøyede rettigheter."""
    if elevated:
        command = f"Start-Process PowerShell -Verb runAs -ArgumentList '-NoExit','-Command \"& \'{command}\'\"'"
    process = subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    if process.returncode == 0:
        logger.info(f"Kommando: {command}\nOutput: {output}")
        return output
    else:
        logger.error(f"Kommando: {command}\nError: {error}")
        raise Exception(f"PowerShell-kommando mislyktes: {error}")

def install_windows_feature(feature_name):
    """Installerer en Windows-funksjon."""
    return run_powershell_command(f"Install-WindowsFeature -Name {feature_name} -IncludeManagementTools")

def configure_active_directory(domain_name, safe_mode_password):
    """Konfigurerer Active Directory."""
    command = f"Install-ADDSForest -DomainName {domain_name} -SafeModeAdministratorPassword (ConvertTo-SecureString -AsPlainText {safe_mode_password} -Force)"
    return run_powershell_command(command, elevated=True)  # Krever forhøyede rettigheter

def configure_group_policy(policy_name, settings):
    """Konfigurerer en gruppepolicy."""
    command = f"New-GPO -Name '{policy_name}' | New-GPLink -Target 'DC={domain_name},DC=com'"
    run_powershell_command(command)
    for setting, value in settings.items():
        command = f"Set-GPRegistryValue -Name '{policy_name}' -Key '{setting}' -Value '{value}'"
        run_powershell_command(command)

# --- VIRTUALISERINGSFUNKSJONER ---
def ssh_connect(hostname, username, password, port=22):
    """Oppretter SSH-tilkobling til en hypervisor."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)
    return client

def run_ssh_command(client, command):
    """Kjører en kommando over SSH og returnerer utdata."""
    _, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    error = stderr.read().decode()
    if error:
        logger.error(f"SSH-kommando mislyktes: {error}")
        raise Exception(f"SSH-kommando mislyktes: {error}")
    return output

def configure_hypervisor_network(client, network_name, vlan_id):
    """Konfigurerer et nettverk på en hypervisor (ESXi-eksempel)."""
    commands = [
        f"esxcli network vswitch standard add -v {network_name}",
        f"esxcli network vswitch standard portgroup add -v {network_name} -p {network_name}",
        f"esxcli network vswitch standard portgroup set -p {network_name} -v {vlan_id}"
    ]
    for cmd in commands:
        run_ssh_command(client, cmd)

def install_hypervisor(hostname, username, password):
    """Installerer og konfigurerer en hypervisor."""
    client = ssh_connect(hostname, username, password)
    configure_hypervisor_network(client, 'VM_Network', 100)
    client.close()

# --- HOVEDPROGRAM ---
def main():
    logger.info("Starter konfigurasjon av Windows Server og virtualisering...")

    # Installasjon av Windows-funksjoner
    install_windows_feature('AD-Domain-Services')
    install_windows_feature('DNS')

    # Konfigurer Active Directory
    domain_name = 'example.com'
    safe_mode_password = getpass.getpass("Skriv inn SafeModeAdministratorPassword: ")
    configure_active_directory(domain_name, safe_mode_password)

    # Konfigurer gruppepolicy
    policy_settings = {
        'HKLM\\Software\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU': 'NoAutoUpdate'
    }
    configure_group_policy('DisableAutoUpdate', policy_settings)

    # Installasjon og konfigurasjon av hypervisor
    hypervisor_password = getpass.getpass("Skriv inn hypervisor-passordet: ")
    install_hypervisor('192.168.1.100', 'root', hypervisor_password)

    logger.info("Konfigurasjon av Windows Server og virtualisering fullført.")

if __name__ == "__main__":
    main()