"""
AUTHORS: 
1- Mohammad Reza momenei
2- Seyed Mohammad Mahdi Niknam Bagheri
"""

from cryptography.fernet import Fernet
# this library encodes bytes into base 64 that is needed by Fernet
import base64
# this library is used to generate symmetric key
import secrets

# Generate a 32-byte random hexadecimal string
key = secrets.token_hex(16)
# converting key to bytes
key = key.encode("utf-8")


def encode(msg, key):
    # creating cipher
    cipher = Fernet(base64.b64encode(key))
    # converting message to bytes
    byte_msg = msg.encode("utf-8")
    # encrypting
    return cipher.encrypt(byte_msg)

def decode(msg, key):
    # creating cipher
    cipher = Fernet(base64.b64encode(key))
    # decrypting
    return cipher.decrypt(msg).decode("utf-8")

if __name__=="__main__":
    test = "hey"
    t = encode(test, key)
    print(decode(t, key))