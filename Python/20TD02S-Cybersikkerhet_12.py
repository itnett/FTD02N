python
import socket

def scan_ports(ip):
    open_ports = []
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

ip_address = '192.168.1.1'
open_ports = scan_ports(ip_address)
print(f"Åpne porter på {ip_address}: {open_ports}")