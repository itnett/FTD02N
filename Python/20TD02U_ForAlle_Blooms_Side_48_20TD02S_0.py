python
from Crypto.Cipher import AES
import base64

def pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def encrypt(message, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt(encrypted_message, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decoded = base64.b64decode(encrypted_message)
    decrypted = cipher.decrypt(decoded).decode('utf-8')
    return decrypted.rstrip(chr(decrypted[-1]))

key = 'ThisIsASecretKey'
message = 'ConfidentialData'
encrypted = encrypt(message, key)
print(f"Encrypted: {encrypted}")
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")