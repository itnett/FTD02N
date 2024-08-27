python
import subprocess
import paramiko
import logging

# Sett opp logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- POWERSHELL-FUNKSJONER FOR WINDOWS SERVER ---
def run_powershell_command(command):
    """Kjører en PowerShell-kommando og returnerer output."""
    process = subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, error = process.communicate()
    if process.returncode == 0:
        logger.info(f"Kommando: {command}\nOutput: {result.decode()}")
        return result.decode()
    else:
        logger.error(f"Kommando: {command}\nError: {error.decode()}")
        return None

def install_windows_feature(feature_name):
    """Installerer en Windows-funksjon."""
    command = f"Install-WindowsFeature -Name {feature_name}"
    return run_powershell_command(command)

def configure_active_directory(domain_name, safe_mode_password):
    """Konfigurerer Active Directory."""
    command = f"Install-ADDSForest -DomainName {domain_name} -SafeModeAdministratorPassword (ConvertTo-SecureString -AsPlainText {safe_mode_password} -Force)"
    return run_powershell_command(command)

def configure_group_policy(policy_name, settings):
    """Konfigurerer en gruppepolicy."""
    command = f"New-GPO -Name '{policy_name}' | New-GPLink -Target 'DC=domain,DC=com'"
    run_powershell_command(command)
    for setting, value in settings.items():
        command = f"Set-GPRegistryValue -Name '{policy_name}' -Key '{setting}' -Value '{value}'"
        run_powershell_command(command)

# --- KONFIGURASJON AV VIRTUALISERINGSMILJØER ---
def ssh_connect(hostname, port, username, password):
    """Oppretter en SSH-tilkobling til en hypervisor."""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        logger.info(f"SSH-tilkobling til {hostname} opprettet.")
        return client
    except (paramiko.AuthenticationException, paramiko.SSHException, socket.error) as e:
        logger.error(f"SSH-tilkobling mislyktes: {e}")
        return None

def run_command(client, command):
    """Kjører en kommando på en hypervisor via SSH."""
    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        logger.info(f"Kommando: {command}\nOutput: {output}")
        return output
    except paramiko.SSHException as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")
        return None

def configure_hypervisor_network(client, network_name, vlan_id):
    """Konfigurerer et nettverk på en hypervisor."""
    commands = [
        f"esxcli network vswitch standard add --vswitch-name={network_name}",
        f"esxcli network vswitch standard portgroup add --portgroup-name={network_name} --vswitch-name={network_name}",
        f"esxcli network vswitch standard portgroup set --portgroup-name={network_name} --vlan-id={vlan_id}"
    ]
    for cmd in commands:
        run_command(client, cmd)
    logger.info(f"Nettverk {network_name} med VLAN {vlan_id} konfigurert på hypervisor.")

def install_hypervisor(hostname, username, password):
    """Installerer og konfigurerer en hypervisor."""
    client = ssh_connect(hostname, 22, username, password)
    if client:
        configure_hypervisor_network(client, network_name='VM_Network', vlan_id=100)
        client.close()

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_windows_server_and_virtualization_examples():
    logger.info("Starter eksempler på Windows Server og virtualisering...")

    # Installasjon av Windows-funksjoner
    install_windows_feature('AD-Domain-Services')
    install_windows_feature('DNS')

    # Konfigurer Active Directory
    configure_active_directory('example.com', 'P@ssw0rd')

    # Konfigurer gruppepolicy
    policy_settings = {
        'HKLM\\Software\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU': 'NoAutoUpdate'
    }
    configure_group_policy('DisableAutoUpdate', policy_settings)

    # Installasjon og konfigurasjon av hypervisor
    install_hypervisor('192.168.1.100', 'root', 'root_password')

    logger.info("Eksempler på Windows Server og virtualisering fullført.")

if __name__ == "__main__":
    run_windows_server_and_virtualization_examples()