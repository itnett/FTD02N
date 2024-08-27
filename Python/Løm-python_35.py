python
class Feriepenger:
    def __init__(self, årslønn, feriepengesats):
        self.årslønn = årslønn
        self.feriepengesats = feriepengesats / 100

    def beregn_feriepenger(self):
        return self.årslønn * self.feriepengesats

feriepenger = Feriepenger(400000, 12)
print(f"Feriepenger: {feriepenger.beregn_feriepenger()}")