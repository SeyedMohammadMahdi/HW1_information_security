from cryptography.fernet import Fernet
import base64
import secrets

# Generate a 32-byte random hexadecimal string
key = secrets.token_hex(16)

key = key.encode("utf-8")


def encode(msg, key):
    cipher = Fernet(base64.b64encode(key))
    byte_msg = msg.encode("utf-8")
    return cipher.encrypt(byte_msg)

def decode(msg, key):
    cipher = Fernet(base64.b64encode(key))
    return cipher.decrypt(msg).decode("utf-8")

if __name__=="__main__":
    test = "hey"
    t = encode(test, key)
    print(decode(t, key))