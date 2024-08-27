python
import socket

# UDP server
def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 12000))
    print("UDP server up and listening...")
    while True:
        message, address = server_socket.recvfrom(1024)
        print(f"Received message: {message} from {address}")
        server_socket.sendto(b"Hello, Client", address)

# UDP client
def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"Hello, Server", ("localhost", 12000))
    message, address = client_socket.recvfrom(1024)
    print(f"Received message: {message} from {address}")

# To run the server or client, uncomment the appropriate function call:
# udp_server()
# udp_client()