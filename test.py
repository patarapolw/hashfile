from hashfile import pass2key
from hashfile.encrypt import encrypt_file
from hashfile.decrypt import decrypt_file, decrypt_filestream

if __name__ == '__main__':
    encrypt_file(pass2key(input('Enter a password: ')), 'cred/secrets.yaml')
    decrypt_file(pass2key(input('Enter your unlock password: ')), 'cred/secrets.yaml.enc')
    print(decrypt_filestream(pass2key(input('Enter your unlock password: ')), 'cred/secrets.yaml.enc'))
