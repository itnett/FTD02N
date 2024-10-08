python
from cryptography.fernet import Fernet

# Generer en nøkkel
nøkkel = Fernet.generate_key()
cipher = Fernet(nøkkel)

# Krypter data og skriv til fil
data = b"Dette er sensitiv data."
kryptert_data = cipher.encrypt(data)
with open('kryptert_fil.dat', 'wb') as fil:
    fil.write(kryptert_data)