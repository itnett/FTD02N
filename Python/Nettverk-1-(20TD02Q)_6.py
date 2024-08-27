python
import socket

def test_tcp_connection(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print(f"TCP-port {port} på {host} er åpen.")
        sock.close()
    except ConnectionRefusedError:
        print(f"TCP-port {port} på {host} er lukket.")

test_tcp_connection("www.example.com", 80)  # Test port 80 (HTTP)