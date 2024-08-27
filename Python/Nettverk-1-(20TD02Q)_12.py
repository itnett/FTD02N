python
import socket

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.error as err:
        return f"DNS-oppslag feilet: {err}"

print(get_ip("www.example.com"))