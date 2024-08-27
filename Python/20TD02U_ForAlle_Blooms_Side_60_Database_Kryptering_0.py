python
from cryptography.fernet import Fernet

# Generere en nøkkel for kryptering
nøkkel = Fernet.generate_key()
cipher = Fernet(nøkkel)

# Kryptere en melding
melding = "Dette er en sensitiv melding."
kryptert_melding = cipher.encrypt(melding.encode())

# Dekryptere meldingen
dekryptert_melding = cipher.decrypt(kryptert_melding).decode()

print("Kryptert:", kryptert_melding)
print("Dekryptert:", dekryptert_melding)