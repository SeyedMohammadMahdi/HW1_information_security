import hashlib

def validator(data, hashed):
    bdata = data.encode("utf-8")
    hasher = hashlib.sha256()
    hasher.update(bdata)
    newhash = hasher.hexdigest()
    print(newhash)
    if(newhash == hashed):
        return True
    else:
        return False