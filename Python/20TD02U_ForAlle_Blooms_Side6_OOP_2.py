python
class Dyr:
    def __init__(self, navn):
        self.navn = navn
    
    def lag_lyd(self):
        print("Et generisk dyrelyd")

class Hund(Dyr):
    def lag_lyd(self):
        print("Voff!")

class Katt(Dyr):
    def lag_lyd(self):
        print("Mjau!")

fido = Hund("Fido")
fido.lag_lyd()  # Utdata: Voff!

pusi = Katt("Pusi")
pusi.lag_lyd()  # Utdata: Mjau!