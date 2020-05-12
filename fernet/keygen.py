import security as s

fernet = s.security()
with open('log.cfg','w') as key_file:
    username = input("Type in your username: ").strip()
    key = fernet.key_gen(username).decode()
    key_file.write(key)