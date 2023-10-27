import socket 
from threading import Thread

def receive():
    host = "localhost"
    port = 1235
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    while(True):
        conn, addr = server.accept()
        data = conn.recv(1024)
        print(data.decode("utf-8"))
        conn.close()
        if(data.decode() == "close"):
            server.close()
            break

def send():
    host = "localhost"
    port = 1234
    while(True):
        sct  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sct.connect((host, port))
            data = input()
            sct.send(data.encode("utf-8"))
            sct.close()
            if(data == "close"):
                return
        except:
            pass


sd = Thread(target=send)
rc = Thread(target=receive)

sd.start()
rc.start()

sd.join()
rc.join()
print("done")