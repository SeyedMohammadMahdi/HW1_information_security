import rsa

(u_key, r_key) = rsa.newkeys(1024)

def encrypt(msg, u_key):
    byte_msg = msg.encode("utf-8")
    encrypted_msg = rsa.encrypt(byte_msg, u_key)
    return encrypted_msg

def decrypt(msg, r_key):
    decrypted_msg = rsa.decrypt(msg, r_key)
    return decrypted_msg.decode("utf-8")

if __name__ == "__main__":
    t = encrypt("hello", u_key)
    print(decrypt(t, r_key))