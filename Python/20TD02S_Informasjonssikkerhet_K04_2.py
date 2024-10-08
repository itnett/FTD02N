python
import hashlib

# Norsk: Funksjon for å beregne SHA-256 hash av data
# English: Function to compute SHA-256 hash of data
def hash_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

# Norsk: Data som skal hashes
# English: Data to be hashed
data = b'Hello, this is a test message!'
hash_value = hash_sha256(data)
print(f"SHA-256 hash: {hash_value}")