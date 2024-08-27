python
class Katt:
    def lag_lyd(self):
        print("Mjau!")

class Hund:
    def lag_lyd(self):
        print("Voff!")

dyr = [Katt(), Hund()]
for d in dyr:
    d.lag_lyd()