python
import subprocess

def run_powershell_command(command):
    process = subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, error = process.communicate()
    if process.returncode == 0:
        logger.info(f"Kommando: {command}\nOutput: {result.decode()}")
        return result.decode()
    else:
        logger.error(f"Kommando: {command}\nError: {error.decode()}")
        return None

def install_windows_feature(feature_name):
    command = f"Install-WindowsFeature -Name {feature_name}"
    return run_powershell_command(command)

def configure_active_directory(domain_name, safe_mode_password):
    command = f"Install-ADDSForest -DomainName {domain_name} -SafeModeAdministratorPassword (ConvertTo-SecureString -AsPlainText {safe_mode_password} -Force)"
    return run_powershell_command(command)

def configure_group_policy(policy_name, settings):
    command = f"New-GPO -Name '{policy_name}' | New-GPLink -Target 'DC=domain,DC=com'"
    run_powershell_command(command)
    for setting, value in settings.items():
        command = f"Set-GPRegistryValue -Name '{policy_name}' -Key '{setting}' -Value '{value}'"
        run_powershell_command(command)