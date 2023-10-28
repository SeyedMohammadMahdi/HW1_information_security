"""
AUTHORS: 
1- Mohammad Reza momenei
2- Seyed Mohammad Mahdi Niknam Bagheri
"""

import socket
from threading import Thread
from symmetric import *
from asymmetric import *
from hash import *

# __________________NOTE__________________
# the server must be running before client
# ________________________________________

# this method at first receives public key from client,
# then uses that key to send symmetric key to client
def exchange_key():
    # creating connection to client

    host = "localhost"
    port = 1236
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    # receiving connectino 
    conn, addr = server.accept()
    # getting public key from client
    data = conn.recv(1024)
    pkey = data
    # loading public key and creating an object from that
    pkey = rsa.PublicKey.load_pkcs1(pkey)
    # encrypting and sending symmetric key
    data = encrypt(key.decode("utf-8"), pkey)
    conn.send(data)
    conn.close()
    server.close()
    # retrunin the received public key
    return pkey

pkey = exchange_key()


# this method handles incomming data
def receive():
    # creating connection
    host = "localhost"
    port = 1234
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    while(True):
        # accepting incomming conneciton
        conn, addr = server.accept()
        # receiving data
        data = conn.recv(1024)
        # decrypting data using symmetric key
        data = decode(data, key)
        print(data)
        conn.close()
        if(data == "close"):
            server.close()
            break

# this method handles outgoing data
# it gets user input, encrypts it and then sends it to client
def send():
    host = "localhost"
    port = 1235
    while(True):
        # creating connection
        sct  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sct.connect((host, port))
            # getting user input
            data = input()
            # encrypting the hash of data and store it in edata using public key
            edata = encrypt(hashing(data), pkey)
            # sending encrypted hash
            sct.send(edata)
            # ecrypting the data itself using symmetric key
            edata = encode(data, key)
            # sending encrypted data
            sct.send(edata)
            sct.close()
            if(data == "close"):
                return
        except:
            pass

# thread for handling send method
sd = Thread(target=send)
# thread for handling receive method
rc = Thread(target=receive)

sd.start()
rc.start()

sd.join()
rc.join()
print("done")