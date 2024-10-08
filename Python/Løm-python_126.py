python
class IndirekteKostnader:
    def __init__(self, administrasjon, markedsføring, husleie):
        self.administrasjon = administrasjon
        self.markedsføring = markedsføring
        self.husleie = husleie

    def totale_indirekte_kostnader(self):
        return self.administrasjon + self.markedsføring + self.husleie

indirekte_kostnader = IndirekteKostnader(50000, 30000, 20000)
print(f"Totale Indirekte Kostnader: {indirekte_kostnader.totale_indirekte_kostnader()}")