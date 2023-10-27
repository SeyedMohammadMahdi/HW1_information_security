from cryptography.fernet import Fernet
# import os
import base64
# generating symmetric key. it is 256 bits.
# we can use it for 128 and 196 bits encryption
key = b"hskfirksjshrksyegcbfjrpqldcgsiwi"

def encode(msg, key):
    # creating a cipher with the generated key
    cipher = Fernet(base64.b64encode(key))
    # encoding message to bytes
    byte_msg = msg.encode("utf-8")
    # returning the cipher-text
    return cipher.encrypt(byte_msg)

def decode(msg, key):
    # creating cipher with generated key
    cipher = Fernet(base64.b64encode(key))
    # retrun the decrypted message
    print(msg)
    return cipher.decrypt(msg).decode("utf-8")

if __name__=="__main__":
    test = "hey"
    # key = base64.b64encode(key)
    t = encode(test, key)
    print(decode(t, key))
    print(key)