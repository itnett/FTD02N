python
# Trinket-kode for Leksjon 6.10: Løse Likninger Digitalt

import sympy as sp

def los_likning_digitalt(likning):
    x = sp.symbols('x')
   

 likning = sp.sympify(likning)
    løsning = sp.solve(likning, x)
    return løsning

# Eksempelbruk
print("Leksjon 6.10: Løse Likninger Digitalt")
likning = input("Skriv inn likningen (f.eks. 3x + 5 = 20): ")
løsning = los_likning_digitalt(likning)
print(f"Løsningen for likningen '{likning}' er: {løsning}")