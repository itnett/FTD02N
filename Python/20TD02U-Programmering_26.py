python
# Python - Hashing med hashlib
import hashlib
password = "mypassword"
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print(hashed_password)