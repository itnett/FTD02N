python
class Driftsinnbetaling:
    def __init__(self, salg, andre_inntekter):
        self.salg = salg
        self.andre_inntekter = andre_inntekter

    def totale_innbetalinger(self):
        return self.salg + self.andre_inntekter

innbetaling = Driftsinnbetaling(500000, 20000)
print(f"Totale Driftsinnbetalinger: {innbetaling.totale_innbetalinger()}")