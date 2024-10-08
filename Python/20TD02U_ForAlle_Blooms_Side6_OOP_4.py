python
class BankKonto:
    def __init__(self, saldo=0):
        self._saldo = saldo  # Bruker en ledende understrek for å indikere at dette er "privat"
    
    def innskudd(self, beløp):
        if beløp > 0:
            self._saldo += beløp
    
    def uttak(self, beløp):
        if 0 < beløp <= self._saldo:
            self._saldo -= beløp
        else:
            print("Ugyldig transaksjon!")

    def vis_saldo(self):
        return self._saldo

konto = BankKonto(100)
konto.innskudd(50)
konto.uttak(30)
print(konto.vis_saldo())  # Utdata: 120