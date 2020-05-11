import security as s

fernet = s.security()
with open('log.cfg','w') as key_file:
    key = fernet.key_gen().decode()
    key_file.write(key)