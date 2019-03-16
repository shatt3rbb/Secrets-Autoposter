from cryptography.fernet import Fernet
import os,sys
#get key from file

def decrypt(token_encrypted):
    file = open(os.path.abspath(os.path.dirname(sys.argv[0]))+"\\" +"rsa.pt","rb")
    key = file.read()
    file.close
    encrypted = token_encrypted.encode()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted)
    decrypted = decrypted.decode()
    return (decrypted)