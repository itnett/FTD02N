python
class Egenkapital:
    def __init__(self, eiendeler, gjeld):
        self.eiendeler = eiendeler
        self.gjeld = gjeld



    def beregn_egenkapital(self):
        return self.eiendeler - self.gjeld

egenkapital = Egenkapital(1000000, 600000)
print(f"Egenkapital: {egenkapital.beregn_egenkapital()}")