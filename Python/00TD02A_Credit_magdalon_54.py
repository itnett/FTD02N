python
søkeord = "feil"
loggfilavsnitt = """
2023-06-13 10:22:31 INFO Bruker 'admin' logget inn.
2023-06-13 10:25:14 ADVARSEL Ugyldig innloggingsforsøk fra IP-adresse 192.168.1.100.
2023-06-13 10:30:05 INFO Bruker 'bruker1' logget inn.
"""

loggoppføringer = loggfilavsnitt.strip().split("\n")
for indeks, oppføring in enumerate(loggoppføringer):
    if søkeord in oppføring.lower():
        print(f"Funnet '{søkeord}' i linje {indeks + 1}: {oppføring}")