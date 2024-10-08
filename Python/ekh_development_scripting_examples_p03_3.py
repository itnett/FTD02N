python
import socket

def scan_ports(ip, port_range):
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        sock.close()

if __name__ == "__main__":
    target_ip = "192.168.1.1"
    ports = range(1, 1025)
    scan_ports(target_ip, ports)