python
class Sirkel:
    def __init__(self, radius):
        self.radius = radius
    
    def omkrets(self):
        return 2 * 3.14 * self.radius
    
    def areal(self):
        return 3.14 * (self.radius ** 2)

sirkel = Sirkel(5)
print(sirkel.omkrets())  # Utskrift: 31.400000000000002
print(sirkel.areal())    # Utskrift: 78.5