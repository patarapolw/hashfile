# Hashfile

Based on the code from [Python PyCrypto encrypt/decrypt text files with AES](https://stackoverflow.com/a/20868265/9023855) and [AES encryption of files in Python with PyCrypto](https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto/), but also allows decryption to bytecode, without outputting a file.

## Requirements

```
pycrypto
```

## Example

```python
from hashfile import pass2key
from hashfile.encrypt import encrypt_file
from hashfile.decrypt import decrypt_file, decrypt_filestream

if __name__ == '__main__':
    encrypt_file(pass2key(input('Enter a password: ')), 'cred/secrets.yaml')
    decrypt_file(pass2key(input('Enter your unlock password: ')), 'cred/secrets.yaml.enc')
    print(decrypt_filestream(pass2key(input('Enter your unlock password: ')), 'cred/secrets.yaml.enc'))
```
