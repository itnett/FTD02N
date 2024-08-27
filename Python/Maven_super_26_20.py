python
class Konto:
    def __init__(self, saldo=0):
        self.__saldo = saldo  # Private variabler bruker __
    
    def innskudd(self, belop):
        self.__saldo += belop
    
    def uttak(self, belop):
        if belop <= self.__saldo:
            self.__saldo -= belop
        else:
            print("Uttak mislyktes: Ikke nok midler")
    
    def vis_saldo(self):
        return self.__saldo

konto = Konto(100)
konto.innskudd(50)
print(konto.vis_saldo())  # Utskrift: 150