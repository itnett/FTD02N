python
class Driftsmargin:
    def __init__(self, driftsinntekter, driftskostnader):
        self.driftsinntekter = driftsinntekter
        self.driftskostnader = driftskostnader

    def beregn_driftsmargin(self):
        return (self.driftsinntekter - self.driftskostnader) / self.driftsinntekter * 100

margin = Driftsmargin(500000, 350000)
print(f"Driftsmargin: {margin

.beregn_driftsmargin():.2f}%")