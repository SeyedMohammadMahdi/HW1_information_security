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

# this method sends public key to server and the receives the symmetric key
# that is encrypted using that public key
def exchange_key():
    # creating connection
    host = "localhost"
    port = 1236
    sct  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sct.connect((host, port))
    # expoting public key
    pkey = u_key.save_pkcs1()
    # sending public key
    sct.send(pkey)
    # receiving encrypted symmetric key
    data = sct.recv(1024)
    # decrypting symmetric key using private key
    data = decrypt(data, r_key)
    skey = data.encode("utf-8")
    sct.close()
    return skey
    
key = exchange_key()

# this method handles incomming data
# first it receives hashed data encrypted using public key
# next it receives data encrypted using symmetric key
# then it uses a vlaidator method to check if message is valid using hash
def receive():
    host = "localhost"
    port = 1235
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    while(True):
        # creating connection
        conn, addr = server.accept()
        # receivin encrypted hash
        data = conn.recv(1024)
        # decrypting hash using private key
        data = decrypt(data, r_key)
        print(data)
        # getting encrypted data itself
        data2 = conn.recv(1024)
        # decrypting using symmetric key
        data2 = decode(data2, key)
        print(data2)
        # validating data using hash
        print(validator(data2, data))
        conn.close()
        if(data2 == "close"):
            server.close()
            break
# this method handles sending data
# it gets user input, encrypts it using symmetric key
# then sends it to server
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