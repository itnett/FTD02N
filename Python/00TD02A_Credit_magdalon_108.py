python
søkeord = "feil"
loggoppføring = "2023-06-13 10:30:05 FEIL Serverfeil"

if søkeord in loggoppføring.lower():
    print("Funnet feilmelding!")