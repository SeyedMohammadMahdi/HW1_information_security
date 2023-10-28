import socket
from threading import Thread
from symmetric import *
from asymmetric import *
from hash import *

def exchange_key():
    host = "localhost"
    port = 1236
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    conn, addr = server.accept()
    data = conn.recv(1024)
    pkey = data
    pkey = rsa.PublicKey.load_pkcs1(pkey)
    data = encrypt(key.decode("utf-8"), pkey)
    conn.send(data)
    conn.close()
    server.close()
    return pkey

pkey = exchange_key()



def receive():
    host = "localhost"
    port = 1234
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    while(True):
        conn, addr = server.accept()
        data = conn.recv(1024)
        data = decode(data, key)
        print(data)
        conn.close()
        if(data == "close"):
            server.close()
            break

def send():
    host = "localhost"
    port = 1235
    while(True):
        sct  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sct.connect((host, port))
            data = input()
            edata = encrypt(hashing(data), pkey)
            sct.send(edata)

            edata = encode(data, key)
            sct.send(edata)
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