import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 1234

server.bind((host, port))

server.listen(1)

conn, addr = server.accept()

data = conn.recv(1024)
print(data.decode())

server.close()