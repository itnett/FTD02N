python
import psutil

while True:
    nettverkstilkoblinger = psutil.net_connections()
    for tilkobling in nettverkstilkoblinger:
        if tilkobling.status == "ESTABLISHED" and tilkobling.raddr:
            print(f"Aktiv tilkobling: {tilkobling.pid} - {tilkobling.laddr} -> {tilkobling.raddr}")
    time.sleep(5)  # Sjekk hvert 5. sekund