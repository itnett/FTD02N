python
import hashlib

def hash_passord(passord):
    salt = b'mitt_salt'  # Bruk et unikt og hemmelig salt
    return hashlib.pbkdf2_hmac('sha256', passord.encode(), salt, 100000)

hashed_passord = hash_passord("mitt_passord")
print(hashed_passord)