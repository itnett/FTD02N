python
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Norsk: Funksjon for å signere data med RSA
# English: Function to sign data using RSA
def sign_rsa(private_key, data):
    h = SHA256.new(data)
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

# Norsk: Funksjon for å verifisere signatur med RSA
# English: Function to verify signature using RSA
def verify_rsa(public_key, data, signature):
    h = SHA256.new(data)
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Norsk: Signer og verifiser meldingen
# English: Sign and verify the message
data = b'Hello, this is a test message!'
signature = sign_rsa(private_key, data)
print(f"Signatur: {signature}")

is_valid = verify_rsa(public_key, data, signature)
print(f"Signatur gyldig: {is_valid}")