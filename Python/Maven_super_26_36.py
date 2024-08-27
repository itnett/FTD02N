python
from cryptography.fernet import Fernet

# Generere en nøkkel
nøkkel = Fernet.generate_key()
cipher = Fernet(nøkkel)

# Kryptere data
data = "Hemmelig melding".encode()
kryptert_data = cipher.encrypt(data)
print(kryptert_data)  # Utskrift: Kryptert versjon av "Hemmelig melding"

# Dekryptere data
dekryptert_data = cipher.decrypt(kryptert_data)
print(dekryptert_data.decode())  # Utskrift: Hemmelig melding