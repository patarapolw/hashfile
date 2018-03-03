# Hashfile

Based on the code from [Python PyCrypto encrypt/decrypt text files with AES](https://stackoverflow.com/a/20868265/9023855), [AES encryption of files in Python with PyCrypto](https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto/) and bcrypt password verification, but also allows decryption to bytecode, without outputting a file.

## Requirements

```
pycrypto
bcrypt
```

## Example

```python
from hashfile.AES.encrypt import encrypt_file
from hashfile.AES.decrypt import decrypt_file, decrypt_filestream

if __name__ == '__main__':
    encrypt_file('password', 'cred/secrets.yaml')
    
    decrypt_file('wrong', 'cred/secrets.yaml.enc')
    decrypt_file('password', 'cred/secrets.yaml.enc')
    
    print(decrypt_filestream('wrong', 'cred/secrets.yaml.enc'))
    print(decrypt_filestream('password', 'cred/secrets.yaml.enc'))
```
Result:

```
Wrong password
Wrong password
False
b"bank1:\n  username: 'asdfg'\n  password: 'asderthb'\n\nbank2:\n  username: 'sdjsio'\n  password: 'pokmmbjh'\n"
```
