python
import ipaddress

def valider_ip_og_port():
    while True:
        ip_adresse = input("Skriv inn en IP-adresse: ")
        port = input("Skriv inn et portnummer (1-65535): ")

        try:
            ipaddress.ip_address(ip_adresse)
            port = int(port)
            if 1 <= port <= 65535:
                return ip_adresse, port
            else:
                print("Ugyldig portnummer.")
        except ValueError:
            print("Ugyldig IP-adresse eller portnummer.")

ip_adresse, port = valider_ip_og_port()
print(f"IP-adresse: {ip_adresse}, Port: {port}")