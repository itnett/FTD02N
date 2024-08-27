python
# Eksempel på loggdata (i virkeligheten vil dette komme fra en fil eller en database)
log_data = [
    {"ip": "192.168.1.10", "status": "failed", "user": "admin"},
    {"ip": "192.168.1.15", "status": "failed", "user": "admin"},
    {"ip": "192.168.1.10", "status": "failed", "user": "admin"},
    {"ip": "192.168.1.20", "status": "success", "user": "user1"},
    {"ip": "192.168.1.10", "status": "failed", "user": "admin"},
]

# Terskelverdi for mistenkelig aktivitet
threshold = 3

# Analyser loggene
ip_attempts = {}
for entry in log_data:
    if entry["status"] == "failed":
        ip_attempts[entry["ip"]] = ip_attempts.get(entry["ip"], 0) + 1

# Identifiser mistenkelige IP-adresser
suspicious_ips = [ip for ip, attempts in ip_attempts.items() if attempts >= threshold]

# Rapport
if suspicious_ips:
    print("Mistenkelige IP-adresser funnet:")
    for ip in suspicious_ips:
        print(f"IP: {ip}, Antall mislykkede forsøk: {ip_attempts[ip]}")
else:
    print("Ingen mistenkelig aktivitet funnet.")