from cryptography.fernet import Fernet


class security:
    """Encryption function and decryption function"""

    def key_gen(self):
        return Fernet.generate_key()

    def encryption(self, msg, key):
        return Fernet.encrypt(Fernet(key),msg.encode())

    def decryption(self, msg, key):
        return Fernet.decrypt(Fernet(key),msg).decode()
