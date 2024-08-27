python
class Forsiktighetsprinsippet:
    def __init__(self, forventet_inntekt, forventet_tap):
        self.forventet_inntekt = forventet_inntekt
        self.forventet_tap = forventet_tap

    def beregn_sikker_verdi(self):
        return self.forventet_inntekt - self.forventet_tap

forsiktighet = Forsiktighetsprinsippet(100000, 20000)
print(f"Sikker Verdi: {forsiktighet.beregn_sikker_verdi()}")