python
revisjonsdata = [
    {"kontroll": "Antivirus oppdatert", "status": "OK"},
    {"kontroll": "Brannmur konfigurert", "status": "OK"},
    {"kontroll": "Brukerrettigheter gjennomgått", "status": "Mangelfull"}
]

for kontroll in revisjonsdata:
    print(f"Kontroll: {kontroll['kontroll']}, Status: {kontroll['status']}")