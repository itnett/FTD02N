python
blokkerte_ip_adresser = ["192.168.1.100", "192.168.1.101"]

# Legg til en ny IP-adresse til blokkeringslisten
ny_ip = "192.168.1.102"
if ny_ip not in blokkerte_ip_adresser:
    blokkerte_ip_adresser.append(ny_ip)

# Fjern en IP-adresse fra blokkeringslisten
fjern_ip = "192.168.1.100"
if fjern_ip in blokkerte_ip_adresser:
    blokkerte_ip_adresser.remove(fjern_ip)