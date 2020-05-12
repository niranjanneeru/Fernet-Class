from cryptography.fernet import Fernet
import base64
import hashlib


class security:
    """Encryption function and decryption function"""

    def key_gen(self, key):
        key = hashlib.sha256(key[:32].encode())
        return base64.urlsafe_b64encode(key.hexdigest().encode()[:32])

    def encryption(self, msg, key):
        return Fernet.encrypt(Fernet(key), msg.encode())

    def decryption(self, msg, key):
        return Fernet.decrypt(Fernet(key), msg).decode()
