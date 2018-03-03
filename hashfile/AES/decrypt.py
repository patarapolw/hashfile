from __future__ import print_function
import os, struct
from Crypto.Cipher import AES

import bcrypt


def decrypt_filestream(password, in_filename, chunksize=24*1024):
    stream = bytes()
    with open(in_filename, 'rb') as infile:
        hashed = infile.read(60)
        key = hashed[:16]
        if not bcrypt.checkpw(password.encode(), hashed):
            print('Wrong password')
            return False

        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        while True:
            chunk = infile.read(chunksize)
            if len(chunk) == 0:
                break
            stream += decryptor.decrypt(chunk)

        stream = stream[0:origsize]

    return stream


def decrypt_file(password, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        hashed = infile.read(60)
        key = hashed[:16]
        if not bcrypt.checkpw(password.encode(), hashed):
            print('Wrong password')
            return False

        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key[:16], AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
