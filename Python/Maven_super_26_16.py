python
class Konto:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def innskudd(self, belop):
        self.saldo += belop
    
    def uttak(self, belop):
        if belop <= self.saldo:
            self.saldo -= belop
        else:
            print("Uttak mislyktes: Ikke nok midler")

konto = Konto(100)
konto.innskudd(50)
print(konto.saldo)  # Utskrift: 150
konto.uttak(70)
print(konto.saldo)  # Utskrift: 80