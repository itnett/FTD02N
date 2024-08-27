python
     class Konto:
         def __init__(self, navn, konto_type):
             self.navn = navn
             self.konto_type = konto_type

         def __repr__(self):
             return f"Konto: {self.navn}, Type: {self.konto_type}"