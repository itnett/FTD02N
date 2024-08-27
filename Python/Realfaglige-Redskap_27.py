python
import bcrypt

passord = b"mitt_hemmelige_passord"
hashed_passord = bcrypt.hashpw(passord, bcrypt.gensalt())

# Senere, for å verifisere:
if bcrypt.checkpw(passord, hashed_passord):
    print("Riktig passord!")