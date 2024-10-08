python
class Flaskehals:
    def __init__(self, produksjonskapasitet, etterspørsel):
        self.produksjonskapasitet = produksjonskapasitet
        self.etterspørsel = etterspørsel

    def beregn_flaskehals(self):
        return min(self.produksjonskapasitet, self.etterspørsel)

flaskehals = Flaskehals(500, 700)
print(f"Flaskehalskapasitet: {flaskehals.beregn_flaskehals()}")