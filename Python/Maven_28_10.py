python
    from getpass import getpass
    import hashlib

    def hash_password(password):
        salt = "5gz".encode()
        return hashlib.sha256(salt + password.encode()).hexdigest()

    password = getpass("Opprett et passord: ")
    hashed_password = hash_password(password)

    print(f"Lagret passord (hashed): {hashed_password}")