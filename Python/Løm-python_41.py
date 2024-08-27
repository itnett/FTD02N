python
class Aksjeselskap:
    def __init__(self, navn, aksjekapital):
        self.navn = navn
        self.aksjekapital = aksjekapital
        self.eiere = []

    def legg_til_eier(self, eier, aksjer):
        self.eiere.append({"eier": eier, "aksjer": aksjer})

    def total_aksjekapital(self):
        return sum(eier["aksjer"] for eier i self.eiere)

as_selskap = Aksjeselskap("TechCorp", 100000)
as_selskap.legg_til_eier("Alice", 50000)
as_selskap.legg_til_eier("Bob", 50000)
print(f"Aksjeselskap: {as_selskap.navn}")
print(f"Total aksjekapital: {as_selskap.total_aksjekapital()}")