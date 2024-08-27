python
class Arbeidsgiveravgift:
    def __init__(self, lønn, sats):
        self.lønn = lønn
        self.sats = sats / 100

    def beregn_arbeidsgiveravgift(self):
        return self.lønn * self.sats

avgift = Arbeidsgiveravgift(500000, 14.1)
print(f"Arbeidsgiveravgift: {avgift.beregn_arbeidsgiveravgift():.2f}")