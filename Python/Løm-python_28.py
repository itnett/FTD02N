python
class Driftsinntekt:
    def __init__(self, salg, tjenester):
        self.salg = salg
        self.tjenester = tjenester

    def totale_inntekter(self):
        return self.salg + self.tjenester

inntekt = Driftsinntekt(400000, 100000)
print(f"Totale Driftsinntekter: {inntekt.totale_inntekter()}")