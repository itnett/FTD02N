python
import hashlib

def hash_passord(passord):
    salt = "tilfeldig_salt"  # Bruk et unikt salt for hvert passord i praksis
    hasher = hashlib.sha256()
    hasher.update(salt.encode() + passord.encode())
    return hasher.hexdigest()

passord = "mittsuperhemmeligePassord"
hashed_passord = hash_passord(passord)
print(hashed_passord)  # Utskrift: Hash-verdi av passordet