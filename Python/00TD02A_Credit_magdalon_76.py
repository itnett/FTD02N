python
import random
import matplotlib.pyplot as plt

class Pakke:
    def __init__(self, størrelse):
        self.størrelse = størrelse

class Nettverkskobling:
    def __init__(self, båndbredde):
        self.båndbredde = båndbredde
        self.kø = []

    def legg_til_pakke(self, pakke):
        self.kø.append(pakke)

    def send_pakker(self, tid):
        sendte_bytes = 0
        while self.kø and sendte_bytes + self.kø[0].størrelse <= self.båndbredde * tid:
            pakke = self.kø.pop(0)
            sendte_bytes += pakke.størrelse
        return sendte_bytes

def simuler_nettverkstrafikk(båndbredde, pakke_størrelser, ankomst_rate, simuleringstid):
    kobling = Nettverkskobling(båndbredde)
    sendte_bytes_per_sekund = []

    for sekund in range(simuleringstid):
        if random.random() < ankomst_rate:
            pakke_størrelse = random.choice(pakke_størrelser)
            kobling.legg_til_pakke(Pakke(pakke_størrelse))
        sendte_bytes = kobling.send_pakker(1)  # Send pakker i ett sekund
        sendte_bytes_per_sekund.append(sendte_bytes)
    return sendte_bytes_per_sekund

# Simuleringskonfigurasjon
båndbredde = 1000  # Kbps
pakke_størrelser = [100, 200, 500]  # Bytes
ankomst_rate = 0.05  # Sannsynlighet for at en pakke ankommer hvert sekund
simuleringstid = 60  # Sekunder

# Kjør simuleringen
sendte_bytes_per_sekund = simuler_nettverkstrafikk(båndbredde, pakke_størrelser, ankomst_rate, simuleringstid)

# Plott resultatene
plt.plot(sendte_bytes_per_sekund)
plt.xlabel("Tid (sekunder)")
plt.ylabel("Sendte bytes per sekund")
plt.title("Simulert nettverkstrafikk")
plt.show()