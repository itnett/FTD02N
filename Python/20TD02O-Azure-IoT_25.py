python
import re

def is_valid_username(username):
    if re.match("^[a-zA-Z0-9_]+$", username):
        return True
    else:
        return False

# Bruk av sikre biblioteker
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"Sensitive Data")
plain_text = cipher_suite.decrypt(cipher_text)