python
    from cryptography.fernet import Fernet

    # Generere en nøkkel for kryptering
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Kryptere en tekst
    plain_text = b"Sensitiv informasjon"
    cipher_text = cipher_suite.encrypt(plain_text)
    print(f"Kryptert tekst: {cipher_text}")

    # Dekryptere teksten
    decrypted_text = cipher_suite.decrypt(cipher_text)
    print(f"Dekryptert tekst: {decrypted_text.decode()}")