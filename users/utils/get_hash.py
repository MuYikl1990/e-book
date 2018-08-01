from hashlib import sha1

def get_hash(str):
    sh = sha1()
    if str:
        sh.update(str.encode('utf8'))
    else:
        return None
    return sh.hexdigest()