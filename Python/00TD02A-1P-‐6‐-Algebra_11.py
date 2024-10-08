python
# Trinket-kode for Leksjon 6.12: Ombygging av Formler

import sympy as sp

def ombygging_av_formler(formel, variabel):
    var = sp.symbols(variabel)
    formel = sp.sympify(formel)
    ombygd_formel = sp.solve(formel, var)
    return ombygd_formel

# Eksempelbruk
print("Leksjon 6.12: Ombygging av Formler")
formel = input("Skriv inn formelen (f.eks. A = pi*r**2): ")
variabel = input("Hvilken variabel vil du isolere? ")
resultat = ombygging_av_formler(formel, variabel)
print(f"Den ombygde formelen for {variabel} er: {resultat}")