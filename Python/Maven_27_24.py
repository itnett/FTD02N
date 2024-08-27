python
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    plain_text = b"Sensitive Data"
    cipher_text = cipher_suite.encrypt(plain_text)
    print(f"Kryptert tekst: {cipher_text}")

    decrypted_text = cipher_suite.decrypt(cipher_text)
    print(f"Dekryptert tekst: {decrypted_text}")