python
class Sirkel:
    def __init__(self, radius):
        self.radius = radius
    
    def areal(self):
        return 3.14 * (self.radius ** 2)

min_sirkel = Sirkel(5)
print(min_sirkel.areal())  # Utdata: 78.5