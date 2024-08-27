python
class Egenkapitalrentabilitet:
    def __init__(self, netto_resultat, egenkapital):
        self.netto_resultat = netto_resultat
        self.egenkapital = egenkapital

    def beregn_egenkapitalrentabilitet(self):
        return (self.netto_resultat / self.egenkapital) * 100

rentabilitet = Egenkapitalrentabilitet(50000, 400000)
print(f"Egenkapitalrentabilitet: {rentabilitet.beregn_egenkapitalrentabilitet():.2f}%")