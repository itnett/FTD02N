python
    import hashlib

    def hash_password(password):
        salt = "5gz".encode()  # Simpel salt
        return hashlib.sha256(salt + password.encode()).hexdigest()

    hashed_password = hash_password("my_secure_password")
    print(f"Hashed Password: {hashed_password}")