python
import paramiko

def configure_vlan(switch_ip, username, password, vlan_id, vlan_name):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(switch_ip, username=username, password=password)

    commands = [
        f"configure terminal",
        f"vlan {vlan_id}",
        f"name {vlan_name}",
        f"exit",
        f"end",
        f"write memory"
    ]

    for cmd in commands:
        stdin, stdout, stderr = client.exec_command(cmd)
        stdout.channel.recv_exit_status()

    client.close()

configure_vlan('192.168.1.1', 'admin', 'password', 10, 'Sales')