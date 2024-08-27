python
from cryptography.fernet import Fernet

# Generer og lagre nøkkel
nøkkel = Fernet.generate_key()
fernet = Fernet(nøkkel)

# Krypter en melding
melding = "Dette er en sikker melding"
kryptert = fernet.encrypt(melding.encode())
print(kryptert)

# Dekrypter meldingen
dekryptert = fernet.decrypt(kryptert).decode()
print(dekryptert)