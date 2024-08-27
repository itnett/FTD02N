python
class Ferielønn:
    def __init__(self, årslønn, feriepengesats):
        self.årslønn = årslønn
        self.feriepengesats = feriepengesats / 100

    def beregn_ferielønn(self):
        return self.årslønn * self.feriepengesats

ferielønn = Ferielønn(400000, 12)
print(f"Ferielønn: {ferielønn.beregn_ferielønn()}")