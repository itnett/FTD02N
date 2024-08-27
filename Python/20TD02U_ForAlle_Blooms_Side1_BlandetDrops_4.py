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

dyr = [Hund("Fido"), Katt("Pusi"), Dyr("Ukjent dyr")]
for dyr in dyr:
    dyr.lag_lyd()