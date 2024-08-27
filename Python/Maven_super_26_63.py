python
import hashlib

data = "min_sikker_data".encode()
hashed = hashlib.sha256(data).hexdigest()
print(hashed)