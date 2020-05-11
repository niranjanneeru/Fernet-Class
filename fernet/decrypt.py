import security as s

fernet = s.security()


def decryptor(msg, key):
    decrypted = fernet.decryption(msg.encode(), key)
    print(decrypted)



try:
    key_file = open('log.cfg')
    key = key_file.read().strip().encode()
    if key is None:
        print('Try running keygen.py')
        quit()
except:
    print('Try running keygen.py')
    quit()

if input("Enter 1 for File input mode or skip: ") == '1':
    with open('database.txt') as file:
        msg = file.read().strip()
else:
    msg = input("Enter Encrrypted Text: ")

decryptor(msg, key)
