python
import hashlib

password = 'mysecretpassword'
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print(hashed_password)