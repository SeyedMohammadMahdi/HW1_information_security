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