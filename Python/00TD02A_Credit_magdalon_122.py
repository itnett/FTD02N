python
import csv
import datetime

def analyser_sikkerhetslogg(filnavn):
    mistenkelige_ip_adresser = {}
    with open(filnavn, "r", newline="") as csvfile:
        leser = csv.DictReader(csvfile, delimiter=",")
        for rad in leser:
            tidspunkt = datetime.datetime.strptime(rad["Tidspunkt"], "%Y-%m-%d %H:%M:%S")
            if rad["Hendelse"] == "Mislykket innlogging":
                ip_adresse = rad["IP-adresse"]
                if ip_adresse not in mistenkelige_ip_adresser:
                    mistenkelige_ip_adresser[ip_adresse] = 0
                mistenkelige_ip_adresser[ip_adresse] += 1
    return mistenkelige_ip_adresser

mistenkelige_ip_adresser = analyser_sikkerhetslogg("sikkerhet.csv")
print("Mistenkelige IP-adresser:")
for ip_adresse, antall_forsøk in mistenkelige_ip_adresser.items():
    print(f"- {ip_adresse}: {antall_forsøk} mislykkede innloggingsforsøk")