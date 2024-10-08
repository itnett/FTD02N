python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_data(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    return iv + encrypted_data

def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
    return decrypted_data

# Example usage
key = os.urandom(32)  # 256-bit key
data = b"Sensitive Information"
encrypted_data = encrypt_data(data, key)
print(f"Encrypted: {encrypted_data}")
decrypted_data = decrypt_data(encrypted_data, key)
print(f"Decrypted: {decrypted_data}")