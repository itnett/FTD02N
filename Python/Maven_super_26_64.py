python
import bcrypt

passord = b"mitt_sikre_passord"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passord, salt)
print(hashed)

# Verifisere passord
innlogget_passord = b"mitt_sikre_passord"
if bcrypt.checkpw(innlogget_passord, hashed):
    print("Passordet matcher")
else:
    print("Passordet matcher ikke")