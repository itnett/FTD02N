python
class Hund:
    def __init__(self, navn):
        self.navn = navn
    
    def bjeff(self):
        print(f"{self.navn} sier: Voff!")

fido = Hund("Fido")
fido.bjeff()  # Utdata: Fido sier: Voff!