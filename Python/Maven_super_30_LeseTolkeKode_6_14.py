python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_rsa_keypair():
    """
    Genererer et RSA nøkkelpar (privat og offentlig nøkkel).
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_data_rsa(data, public_key):
    """
    Krypterer data med RSA og offentlig nøkkel.
    """
    encrypted = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def decrypt_data_rsa(encrypted_data, private_key):
    """
    Dekrypterer data med RSA og privat nøkkel.
    """
    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted

def main():
    # Generer RSA nøkkelpar
    private_key, public_key = generate_rsa_keypair()
    print("RSA keys generated.")

    # Krypter en melding
    message = b"This is a secret message."
    encrypted_message = encrypt_data_rsa(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")

    # Dekrypter meldingen
    decrypted_message = decrypt_data_rsa(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message.decode()}")

if __name__ == "__main__":
    main()