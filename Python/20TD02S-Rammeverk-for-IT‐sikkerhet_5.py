python
for kontroll in revisjonsdata:
    if kontroll['status'] != "OK":
        print(f"Forbedringsplan nødvendig for: {kontroll['kontroll']}")