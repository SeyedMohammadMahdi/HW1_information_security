import rsa

# generate public and private keys
(u_key, r_key) = rsa.newkeys(1024)

def encrypt(msg, u_key):
    # convert message to bytes
    byte_msg = msg.encode("utf-8")
    # encrypting the message
    encrypted_msg = rsa.encrypt(byte_msg, u_key)
    return encrypted_msg

def decrypt(msg, r_key):
    # decrypting the message
    decrypted_msg = rsa.decrypt(msg, r_key)
    # converting the decrypted message to string
    return decrypted_msg.decode("utf-8")

if __name__ == "__main__":
    t = encrypt("hello", u_key)
    print(decrypt(t, r_key))