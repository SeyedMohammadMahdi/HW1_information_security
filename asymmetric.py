"""
AUTHORS: 
1- Mohammad Reza momenei
2- Seyed Mohammad Mahdi Niknam Bagheri
"""

import rsa
# creating public and private keys
(u_key, r_key) = rsa.newkeys(1024)

def encrypt(msg, u_key):
    # converting message to bytes
    byte_msg = msg.encode("utf-8")
    # encrypting using public key
    encrypted_msg = rsa.encrypt(byte_msg, u_key)
    return encrypted_msg

def decrypt(msg, r_key):
    # decrypting using private key
    decrypted_msg = rsa.decrypt(msg, r_key)
    return decrypted_msg.decode("utf-8")

if __name__ == "__main__":
    t = encrypt("hello", u_key)
    print(decrypt(t, r_key))