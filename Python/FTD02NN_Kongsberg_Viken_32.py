python
import paramiko

def configure_device(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)
    
    commands = [
        "configure terminal",
        "hostname NewRouter",
        "interface GigabitEthernet0/0",
        "ip address 192.168.1.1 255.255.255.0",
        "no shutdown",
        "exit",
        "exit"
    ]
    
    for command in commands:
        ssh.exec_command(command)
    
    ssh.close()

configure_device("192.168.1.1", "admin", "password")