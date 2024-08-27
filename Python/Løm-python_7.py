python
class FasteKostnader:
    def __init__(self, husleie, forsikring, faste_lønninger):
        self.husleie = husleie
        self.forsikring = forsikring
        self.faste_lønninger = faste_lønninger

    def totale_faste_kostnader(self):
        return self.husleie + self.forsikring + self.faste_lønninger

faste_kostnader = FasteKostnader(10000, 5000, 20000)
print(f"Totale Faste Kostnader: {faste_kostnader.totale_faste_kostnader()}")