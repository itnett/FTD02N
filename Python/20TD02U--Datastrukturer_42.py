python
import hashlib

def store_password(password):
    # Bruk en kryptografisk sikker hashfunksjon
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Lagre den hashede passordet sikkert
    print(hashed_password)

store_password("my_secure_password")