import rsa

(u_key, r_key) = rsa.newkeys(1024)

def u_encrypt(msg):
    byte_msg = msg.encode("utf-8")
    encrypted_msg = rsa.encrypt(byte_msg, u_key)
    return encrypted_msg

def r_decrypt(msg):
    decrypted_msg = rsa.decrypt(msg, r_key)
    return decrypted_msg.decode("utf-8")

if __name__ == "__main__":
    t = u_encrypt("hello")
    print(r_decrypt(t))