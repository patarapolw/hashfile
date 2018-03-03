# import hashlib
import bcrypt


def pass2key(password):
    # return hashlib.sha256(password.encode()).digest()
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
