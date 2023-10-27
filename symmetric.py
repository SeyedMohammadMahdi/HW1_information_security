from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encode(msg):
    byte_msg = msg.encode("utf-8")
    return cipher.encrypt(byte_msg)

def decode(msg):
    return cipher.decrypt(msg).decode("utf-8")

if __name__=="__main__":
    test = "hey"
    t = encode(test)
    print(decode(t))