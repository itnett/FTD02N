python
from cryptography.fernet import Fernet

# Generer en nøkkel
nøkkel = Fernet.generate_key()
cipher = Fernet(nøkkel)

# Krypter en melding
melding = b"Dette er hemmelig"
kryptert_melding = cipher.encrypt(melding)

# Dekrypter meldingen
dekryptert_melding = cipher.decrypt(kryptert_melding)
print(dekryptert_melding)