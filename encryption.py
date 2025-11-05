from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


class DataEncryption:
    def __init__(self, key):
        self.key = key.encode() if isinstance(key, str) else key

    def encrypt_data(self, plaintext):
        """Encrypt data using AES"""
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

    def decrypt_data(self, encrypted_data):
        """Decrypt AES encrypted data"""
        data = base64.b64decode(encrypted_data)
        nonce = data[:16]
        tag = data[16:32]
        ciphertext = data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode()
