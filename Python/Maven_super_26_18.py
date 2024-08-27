python
class Dyr:
    def __init__(self, navn):
        self.navn = navn
    
    def lag_lyd(self):
        pass

class Hund(Dyr):
    def lag_lyd(self):
        return "Bjeff"

class Katt(Dyr):
    def lag_lyd(self):
        return "Mjau"

hund = Hund("Fido")
katt = Katt("Misty")
print(hund.lag_lyd())  # Utskrift: Bjeff
print(katt.lag_lyd())  # Utskrift: Mjau