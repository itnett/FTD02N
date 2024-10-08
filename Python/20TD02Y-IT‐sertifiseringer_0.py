python
import socket

# Opprett en socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Koble til en server
s.connect(('www.example.com', 80))

# Send en HTTP-forespørsel
request = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
s.send(request.encode())

# Motta responsen
response = s.recv(4096)
print(response.decode())

# Lukk socket
s.close()