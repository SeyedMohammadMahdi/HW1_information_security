import socket 
from threading import Thread
from symmetric import *
from asymmetric import *
from hash import *


def exchange_key():
    host = "localhost"
    port = 1236
    sct  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sct.connect((host, port))
    pkey = u_key.save_pkcs1()
    sct.send(pkey)
    data = sct.recv(1024)
    data = decrypt(data, r_key)
    skey = data.encode("utf-8")
    sct.close()
    return skey
    
key = exchange_key()

# print(skey)
def receive():
    host = "localhost"
    port = 1235
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    while(True):
        conn, addr = server.accept()
        data = conn.recv(1024)
        data = decrypt(data, r_key)
        print(data)

        data2 = conn.recv(1024)
        data2 = decode(data2, key)
        print(data2)
        print(validator(data2, data))
        conn.close()
        if(data2 == "close"):
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