python
class Hund:
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
    
    def bjeff(self):
        print(f"{self.navn} sier: Voff!")
    
    def beregn_hund_år(self):
        return self.alder * 7

fido = Hund("Fido", 4)
fido.bjeff()  # Utdata: Fido sier: Voff!
print(fido.beregn_hund_år())  # Utdata: 28