python
# Trinket-kode for Leksjon 6.5: Løse opp Parenteser

def los_opp_parenteser(uttrykk):
    return eval(uttrykk)

# Eksempelbruk
print("Leksjon 6.5: Løse opp Parenteser")
uttrykk = input("Skriv inn et uttrykk med parenteser (f.eks. 3*(a + 2)): ")
resultat = los_opp_parenteser(uttrykk)
print(f"Resultatet av {uttrykk} er {resultat}")