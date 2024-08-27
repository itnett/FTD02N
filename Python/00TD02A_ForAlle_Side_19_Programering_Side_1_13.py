python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encrypted_text = cipher_suite.encrypt(b"Hello, World!")
decrypted_text = cipher_suite.decrypt(encrypted_text)