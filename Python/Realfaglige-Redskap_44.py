python
class Dyr:
    def __init__(self, navn):
        self.navn = navn

    def lag_lyd(self):
        print("Generisk dyrelyd")

class Hund(Dyr):
    def lag_lyd(self):
        print("Voff!")

class Katt(Dyr):
    def lag_lyd(self):
        print("Mjau!")