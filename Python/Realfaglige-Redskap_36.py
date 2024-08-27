python
class Hund:
    def __init__(self, navn, rase):
        self.navn = navn
        self.rase = rase

    def bjeff(self):
        print("Voff!")

fido = Hund("Fido", "Golden Retriever")
fido.bjeff()  # Output: "Voff!"