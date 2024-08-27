python
# Trinket-kode for Leksjon 6.7: Addisjons- og Subtraksjonsmetoden

import sympy as sp

def addisjon_subtraksjonsmetoden(likning1, likning2):
    x, y = sp.symbols('x y')
    likning1 = sp.sympify(likning1)
    likning2 = sp.sympify(likning2)
    løsning = sp.solve((likning1, likning2), (x, y))
    return løsning

# Eksempelbruk
print("Leksjon 6.7: Addisjons- og Subtraksjonsmetoden")
likning1 = input("Skriv inn første likning (f.eks. x + y = 10): ")
likning2 = input("Skriv inn andre likning (f.eks. x - y = 2): ")
løsning = addisjon_subtraksjonsmetoden(likning1, likning2)
print(f"Løsningen for systemet er: {løsning}")