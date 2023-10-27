from cryptography.fernet import Fernet

key = Fernet.generate_key()


def encode(msg, key):
    cipher = Fernet(key)
    byte_msg = msg.encode("utf-8")
    return cipher.encrypt(byte_msg)

def decode(msg, key):
    cipher = Fernet(key)
    return cipher.decrypt(msg).decode("utf-8")

if __name__=="__main__":
    test = "hey"
    t = encode(test, key)
    print(decode(t, key))