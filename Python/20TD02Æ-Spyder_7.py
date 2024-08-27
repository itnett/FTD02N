python
import paramiko

def ssh_connect(hostname, port, username, password):
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
    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        logger.info(f"Kommando: {command}\nOutput: {output}")
        return output
    except paramiko.SSHException as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")
        return None

def configure_hypervisor_network(client, network_name, vlan_id):
    commands = [
        f"esxcli network vswitch standard add --vswitch-name={network_name}",
        f"esxcli network vswitch standard portgroup add --portgroup-name={network_name} --vswitch-name={network_name}",
        f"esxcli network vswitch standard portgroup set --portgroup-name={network_name} --vlan-id={vlan_id}"
    ]
    for cmd in commands:
        run_command(client, cmd)
    logger.info(f"Nettverk {network_name} med VLAN {vlan_id} konfigurert på hypervisor.")

def install_hypervisor(hostname, username, password):
    client = ssh_connect(hostname, 22, username, password)
    if client:
        configure_hypervisor_network(client, network_name='VM_Network', vlan_id=100)
        client.close()