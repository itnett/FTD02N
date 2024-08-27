python
from cryptography.fernet import Fernet

# Generer en nøkkel og lagre den et trygt sted
nøkkel = Fernet.generate_key()
fernet = Fernet(nøkkel)

# Kryptere data
melding = "Denne meldingen er hemmelig."
kryptert = fernet.encrypt(melding.encode())
print(kryptert)

# Dekryptere data
dekryptert = fernet.decrypt(kryptert).decode()
print(dekryptert)