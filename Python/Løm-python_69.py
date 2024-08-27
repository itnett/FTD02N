python
    class Kunde:
        def __init__(self, navn, kjøpshistorikk):
            self.navn = navn
            self.kjøpshistorikk = kjøpshistorikk

        def analyse_adferd(self):
            return f"Kunde {self.navn} har kjøpt {len(self.kjøpshistorikk)} ganger."

    kunde = Kunde("Eva", ["Produkt A", "Produkt B", "Produkt C"])
    print(kunde.analyse_adferd())