python
class Faktoring:
    def __init__(self, faktura_beløp, rabatt_prosent):
        self.faktura_beløp = faktura_beløp
        self.rabatt_prosent = rabatt_prosent / 100

    def beregn_kontantstrøm(self):
        return self.faktura_beløp * (1 - self.rabatt_prosent)

faktoring = Faktoring(100000, 5)
print(f"Kontantstrøm fra faktoring: {faktoring.beregn_kontantstrøm()}")