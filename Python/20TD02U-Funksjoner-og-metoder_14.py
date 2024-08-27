python
     import hashlib

     def hash_password(password):
         return hashlib.sha256(password.encode()).hexdigest()

     hashed = hash_password("my_secure_password")
     print(hashed)