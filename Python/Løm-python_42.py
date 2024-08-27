python
class Annuitetslån:
    def __init__(self, lånebeløp, rente, antall_terminer):
        self.lånebeløp = lånebeløp
        self.rente = rente / 100
        self.antall_terminer = antall_terminer

    def terminbeløp(self):
        r = self.rente / 12
        n = self.antall_terminer
        return self.lånebeløp * r / (1 - (1 + r) ** -n)

lån = Annuitetslån(1000000, 5, 360)
print(f"Terminbeløp: {lån.terminbeløp():.2f}")