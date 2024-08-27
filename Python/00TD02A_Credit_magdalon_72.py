python
import socket

def sjekk_port_status(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)  # Sett en timeout for å unngå å vente for lenge
    try:
        s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()

host = "www.example.com"
port = 80
if sjekk_port_status(host, port):
    print(f"Port {port} er åpen på {host}")
else:
    print(f"Port {port} er lukket på {host}")