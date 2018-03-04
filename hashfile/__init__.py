import hashlib


def pass2key(password):
    return hashlib.sha256(password.encode()).digest()
