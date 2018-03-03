from hashfile.AES.encrypt import encrypt_file
from hashfile.AES.decrypt import decrypt_file, decrypt_filestream

if __name__ == '__main__':
    encrypt_file('password', 'cred/secrets.yaml')

    decrypt_file('wrong', 'cred/secrets.yaml.enc')
    decrypt_file('password', 'cred/secrets.yaml.enc')

    print(decrypt_filestream('wrong', 'cred/secrets.yaml.enc'))
    print(decrypt_filestream('password', 'cred/secrets.yaml.enc'))
