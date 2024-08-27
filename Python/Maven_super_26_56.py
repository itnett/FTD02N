python
import hashlib

passord = "mitt_sikre_passord"
hashed_passord = hashlib.sha256(passord.encode()).hexdigest()
print(hashed_passord)