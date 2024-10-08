python
import numpy as np

# IP-adresser i et nettverk
ip_adresser = np.array([
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
])

# Finn antall IP-adresser
antall_adresser = ip_adresser.size
print(f"Antall IP-adresser: {antall_adresser}")

# Sjekk om en spesifikk IP-adresse finnes i nettverket
søke_ip = "192.168.1.5"
if søke_ip in ip_adresser:
    print(f"{søke_ip} finnes i nettverket.")
else:
    print(f"{søke_ip} finnes ikke i nettverket.")