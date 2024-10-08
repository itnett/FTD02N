python
import hashlib

def hash_data(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

# Example usage
data = b"Important Data"
hashed_data = hash_data(data)
print(f"Hashed Data: {hashed_data}")