python
import socket

def check_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

ip_address = input("Skriv inn IP-adressen: ")
for port in [22, 80, 443]:
    if check_port(ip_address, port):
        print(f"Port {port} er åpen")
    else:
        print(f"Port {port} er lukket")