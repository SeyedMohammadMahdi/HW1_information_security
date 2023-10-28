"""
AUTHORS: 
1- Mohammad Reza momenei
2- Seyed Mohammad Mahdi Niknam Bagheri
"""

import hashlib

def validator(data, hashed):
    # convertin data to bytes
    bdata = data.encode("utf-8")
    # creating hasher object
    hasher = hashlib.sha256()
    # hashing data
    hasher.update(bdata)
    # getting the hashed data in hexadecimal representation
    newhash = hasher.hexdigest()
    # if the hash is equal to received hash then the message is valid
    # otherwise it is invalid
    if(newhash == hashed):
        return True
    else:
        return False

def hashing(data):
     # convertin data to bytes
    bdata = data.encode("utf-8")
    # creating hasher object
    hasher = hashlib.sha256()
    # hashing data
    hasher.update(bdata)
    # getting the hashed data in hexadecimal representation
    newhash = hasher.hexdigest()

    return newhash

if __name__ == "__main__":
    data = "hey"
    h = hashing(data)
    h = hashing(h)
    print(validator(data, h))
    print(h)