python
class Driftskapital:
    def __init__(self, omløpsmidler, kortsiktig_gjeld):
        self.omløpsmidler = omløpsmidler
        self.kortsiktig_gjeld = kortsiktig_gjeld

    def beregn_driftskapital(self):
        return self.omløpsmidler - self.kortsiktig_gjeld

kapital = Driftskapital(300000, 150000)
print(f"Driftskapital: {kapital.beregn_driftskapital()}")