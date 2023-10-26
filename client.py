import socket 

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 1234

socket.connect((host, port))
data = "hello"
socket.send(data.encode())

socket.close()