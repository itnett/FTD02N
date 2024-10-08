python
loggfilavsnitt = """
2023-06-13 10:22:31 INFO Bruker 'admin' logget inn.
2023-06-13 10:25:14 ADVARSEL Ugyldig innloggingsforsøk fra IP-adresse 192.168.1.100.
2023-06-13 10:30:05 INFO Bruker 'bruker1' logget inn.
"""

# Split loggfilavsnittet inn i en liste av linjer
loggoppføringer = loggfilavsnitt.strip().split("\n")

# Finn antall loggoppføringer
antall_oppføringer = len(loggoppføringer)
print(f"Antall loggoppføringer: {antall_oppføringer}")

# Finn alle unike IP-adresser i loggen
ip_adresser = []
for oppføring in loggoppføringer:
    if "IP-adresse" in oppføring:
        ip_adresse = oppføring.split("IP-adresse ")[1].split(".")[0]
        ip_adresser.append(ip_adresse)

unike_ip_adresser = list(set(ip_adresser))
print(f"Unike IP-adresser: {unike_ip_adresser}")