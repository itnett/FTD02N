python
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a message
text = b"Secret message"
cipher_text = cipher_suite.encrypt(text)

# Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text)