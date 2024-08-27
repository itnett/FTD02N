python
import ipaddress

def valider_ip_adresse(ip_adresse):
    try:
        ipaddress.ip_address(ip_adresse)
        return True
    except ValueError:
        return False

ip_adresse = input("Skriv inn en IP-adresse: ")
if valider_ip_adresse(ip_adresse):
    print("Gyldig IP-adresse")
else:
    print("Ugyldig IP-adresse")