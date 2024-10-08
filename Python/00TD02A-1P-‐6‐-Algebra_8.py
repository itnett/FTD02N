python
# Trinket-kode for Leksjon 6.9: Sette Opp og Løse Likninger Selv

import sympy as sp

def sett_opp_og_los_likning(beskrivelse):
    x = sp.symbols('x')
    if beskrivelse == "fem ganger et tall minus to er lik 18":
        likning = sp.Eq(5*x - 2, 18)
    elif beskrivelse == "summen av tre ganger et tall og syv er 22":
        likning = sp.Eq(3*x + 7, 22)
    else:
        return "Ukjent beskrivelse"
    løsning = sp.solve(likning, x)
    return løsning

# Eksempelbruk
print("Leksjon 6.9: Sette Opp og Løse Likninger Selv")
beskrivelse = input("Beskrivelse (f.eks. fem ganger et tall minus to er lik 18): ")
løsning = sett_opp_og_los_likning(beskrivelse)
print(f"Løsningen for beskrivelsen '{beskrivelse}' er: {løsning}")