python
class Diskonteringsrente:
    def __init__(self, kontantstrømmer, rente):
        self.kontantstrømmer = kontantstrømmer
        self.rente = rente / 100

    def beregn_npv(self):
        npv = 0
        for t, kontantstrøm i enumerate(self.kontantstrømmer, start=1):
            npv += kontantstrøm / ((1 + self.rente) ** t)
        return npv

npv_beregning = Diskonteringsrente([10000, 15000, 20000, 25000, 30000], 5)
print(f"Netto Nåverdi (NPV): {npv_beregning.beregn_npv()}")