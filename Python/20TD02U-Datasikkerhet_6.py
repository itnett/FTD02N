python
import bcrypt

# Hash et passord
password = b"supersecret"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Sjekk passord
if bcrypt.checkpw(password, hashed):
    print("Password matches")
else:
    print("Password does not match")