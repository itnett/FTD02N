python
     class Transaksjon:
         def __init__(self, dato, konto, belop, transaksjon_type):
             self.dato = dato
             self.konto = konto
             self.belop = belop
             self.transaksjon_type = transaksjon_type

         def __repr__(self):
             return f"Transaksjon: {self.dato}, Konto: {self.konto}, Beløp: {self.belop}, Type: {self.transaksjon_type}"