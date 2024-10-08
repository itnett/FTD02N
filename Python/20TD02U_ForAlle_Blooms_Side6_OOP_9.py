python
class Produkt:
    def __init__(self, navn, pris):
        self.navn = navn
        self.pris = pris

class Handlekurv:
    def __init__(self):
        self.produkter = []

    def legg_til(self, produkt):
        self.produkter.append(produkt)

    def total_pris(self):
        return sum([produkt.pris for produkt i self.produkter])

class Bestilling:
    def __init__(self, handlekurv):
        self.handlekurv = handlekurv
        self.status = "Ny"

    def bekreft(self):
        self.status = "Bekreftet"

# Bruk av systemet
produkt1 = Produkt("Bok", 199)
produkt2 = Produkt("PC", 9999)
handlekurv = Handlekurv()
handlekurv.legg_til(produkt1)
handlekurv.legg_til(produkt2)
bestilling = Bestilling(handlekurv)
bestilling.bekreft()

print(f"Total pris: {handlekurv.total_pris()} kr")  # Utdata: 10198 kr