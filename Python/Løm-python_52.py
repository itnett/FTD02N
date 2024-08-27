python
class Etterkalkyle:
    def __init__(self, faktiske_kostnader, forkalkyle):
        self.faktiske_kostnader = faktiske_kostnader
        self.forkalkyle = forkalkyle

    def beregn_avvik(self):
        return self.faktiske_kostnader - self.forkalkyle

etterkalkyle = Etterkalkyle(450000, 400000)
print(f"Avvik: {etterkalkyle.beregn_avvik()}")