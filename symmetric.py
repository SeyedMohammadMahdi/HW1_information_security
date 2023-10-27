from cryptography.fernet import Fernet

# generating symmetric key. it is 256 bits.
# we can use it for 128 and 196 bits encryption
key = Fernet.generate_key()


def encode(msg, key):
    # creating a cipher with the generated key
    cipher = Fernet(key)
    # encoding message to bytes
    byte_msg = msg.encode("utf-8")
    # returning the cipher-text
    return cipher.encrypt(byte_msg)

def decode(msg, key):
    # creating cipher with generated key
    cipher = Fernet(key)
    # retrun the decrypted message
    return cipher.decrypt(msg).decode("utf-8")

if __name__=="__main__":
    test = "hey"
    t = encode(test, key)
    print(decode(t, key))