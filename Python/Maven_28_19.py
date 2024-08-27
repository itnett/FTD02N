python
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes

    def pad(data):
        return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

    def encrypt(key, data):
        data = pad(data)
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(data)

    def decrypt(key, cipher_data):
        iv = cipher_data[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = cipher.decrypt(cipher_data[AES.block_size:])
        return data.rstrip(b"\0")

    key = get_random_bytes(16)
    encrypted = encrypt(key, b"Sensitive information")
    print(f"Kryptert: {encrypted}")

    decrypted = decrypt(key, encrypted)
    print(f"Dekryptert: {decrypted}")