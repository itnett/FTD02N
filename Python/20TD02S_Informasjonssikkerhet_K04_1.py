python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Norsk: Generer RSA-nøkkelpar
# English: Generate RSA key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Norsk: Lagre nøklene til filer
# English: Save the keys to files
with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

# Norsk: Last inn de offentlige og private nøklene
# English: Load the public and private keys
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())
with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Norsk: Funksjon for å kryptere meldinger med RSA
# English: Function to encrypt messages using RSA
def encrypt_rsa(public_key, data):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(data)
    return ciphertext

# Norsk: Funksjon for å dekryptere meldinger med RSA
# English: Function to decrypt messages using RSA
def decrypt_rsa(private_key, ciphertext):
    cipher = PKCS1_OAEP.new(private_key)
    data = cipher.decrypt(ciphertext)
    return data

# Norsk: Krypter og dekrypter meldingen
# English: Encrypt and decrypt the message
data = b'Hello, this is a test message!'
ciphertext = encrypt_rsa(public_key, data)
print(f"Kryptert tekst: {ciphertext}")

decrypted_data = decrypt_rsa(private_key, ciphertext)
print(f"Dekryptert tekst: {decrypted_data.decode()}")