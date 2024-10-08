python
import requests
import time

nettsider = ["https://www.google.com", "https://www.example.com", "https://www.wikipedia.org"]

for nettside in nettsider:
    start_tid = time.time()
    try:
        respons = requests.get(nettside)
        respons.raise_for_status()  # Sjekk for HTTP-feilkoder
        slutt_tid = time.time()
        responstid = slutt_tid - start_tid
        print(f"{nettside}: {responstid:.2f} sekunder")
    except requests.exceptions.RequestException as e:
        print(f"Feil ved henting av {nettside}: {e}")