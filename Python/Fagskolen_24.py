python
class Vare:
    def __init__(self, varenummer, navn, antall, pris):
        self.varenummer = varenummer
        self.navn = navn
        self.antall = antall
        self.pris = pris

    def __str__(self):
        return f"{self.varenummer} - {self.navn} - {self.antall} - {self.pris}"

# Additional classes for Ordre, Ordredetaljer, and Visallekunder