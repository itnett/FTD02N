python
# Import the necessary modules
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Norsk: Funksjon for å kryptere meldinger med AES
# English: Function to encrypt messages using AES
def encrypt_aes(key, data):
    # Create a cipher object using the random key
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    # Encrypt the data
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return nonce, ciphertext, tag

# Norsk: Funksjon for å dekryptere meldinger med AES
# English: Function to decrypt messages using AES
def decrypt_aes(key, nonce, ciphertext, tag):
    # Create a cipher object using the random key and nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    # Decrypt the data
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

# Norsk: Generer en tilfeldig nøkkel
# English: Generate a random key
key = get_random_bytes(16) # 128 bits key
data = b'Hello, this is a test message!'

# Norsk: Krypter meldingen
# English: Encrypt the message
nonce, ciphertext, tag = encrypt_aes(key, data)
print(f"Kryptert tekst: {ciphertext}")

# Norsk: Dekrypter meldingen
# English: Decrypt the message
decrypted_data = decrypt_aes(key, nonce, ciphertext, tag)
print(f"Dekryptert tekst: {decrypted_data.decode()}")