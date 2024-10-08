python
   import pdb
   import socket

   host, port = 'localhost', 12345
   server_socket = socket.socket()
   server_socket.bind((host, port))
   server_socket.listen(1)
   print(f"Debugger running on {host}:{port}")

   conn, addr = server_socket.accept()
   with conn:
       pdb.Pdb(stdin=conn.makefile('rb'), stdout=conn.makefile('wb')).set_trace()