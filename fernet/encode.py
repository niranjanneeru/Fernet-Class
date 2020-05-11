import security as s

fernet = s.security()

def encrypter(msg,key):
    encrypted = fernet.encryption(msg,key).decode()
    with open('database.txt','w') as file:
        file.write(encrypted)



try:
    key_file = open('log.cfg')
    key = key_file.read().strip().encode()
except:
    if key is None:
        print('Try running keygen.py')
        quit()
    print('Try running keygen.py')
    quit()
encrypter(input("Enter the Secret Message: "),key)

