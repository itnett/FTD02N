python
# Import the necessary modules
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib

# Norsk: Generer RSA-nøkkelpar for asymmetrisk kryptering og digital signatur
# English: Generate RSA key pair for asymmetric encryption and digital signature
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()
private_key = RSA.import_key(private_key)
public_key = RSA.import_key(public_key)

# Norsk: Generer en tilfeldig nøkkel for symmetrisk kryptering
# English: Generate a random key for symmetric encryption
aes_key = get_random_bytes(16)

# Data to be encrypted, hashed, and signed
data = b'Hello, this is a comprehensive test message!'

# 1. Symmetrisk Kryptering (AES)
def encrypt_aes(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return nonce, ciphertext, tag

def decrypt_aes(key, nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

nonce, ciphertext_aes, tag = encrypt_aes(aes_key, data)
print(f"Symmetrisk Kryptert tekst: {ciphertext_aes}")
decrypted_data_aes = decrypt_aes(aes_key, nonce, ciphertext_aes, tag)
print(f"Symmetrisk Dekryptert tekst: {decrypted_data_aes.decode()}")

# 2. Asymmetrisk Kryptering (RSA)
def encrypt_rsa(public_key, data):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(data)
    return ciphertext

def decrypt_rsa(private_key, ciphertext):
    cipher = PKCS1_OAEP.new(private_key)
    data = cipher.decrypt(ciphertext)
    return data

ciphertext_rsa = encrypt_rsa(public_key, data)
print(f"Asymmetrisk Kryptert tekst: {ciphertext_rsa}")
decrypted_data_rsa = decrypt_rsa(private_key, ciphertext_rsa)
print(f"Asymmetrisk Dekryptert tekst: {decrypted_data_rsa.decode()}")

# 3. Hashfunksjoner (SHA-256)
def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

hash_value = hash_sha256(data)
print(f"SHA-256 hash: {hash_value}")

# 4. Digital Signatur (RSA)
def sign_rsa(private_key, data):
    h = SHA256.new(data)
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify_rsa(public_key, data, signature):
    h = SHA256.new(data)
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

signature = sign_rsa(private_key, data)
print(f"Signatur: {signature}")
is_valid = verify_rsa(public_key, data, signature)
print(f"Signatur gyldig: {is_valid}")