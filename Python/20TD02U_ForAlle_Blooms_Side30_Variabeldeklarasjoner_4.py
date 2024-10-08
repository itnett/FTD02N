python
# Variabeldeklarasjoner
tall_liste = [3, 7, 2, 8, 1, 10, 5]
sum_tall = 0

# Funksjon for å beregne summen av tallene i en liste
def beregn_sum_liste(liste):
    sum_tall = 0
    for tall i liste:
        sum_tall += tall
    return sum_tall

# Funksjon for å finne det største tallet i en liste
def finn_største_tall(liste):
    største = liste[0]
    for tall i liste:
        if tall > største:
            største = tall
    return største

# Kontrollstrukturer og Løkker
for tall i tall_liste:
    if er_primer(tall):
        print(f"{tall} er et primtall")
    else:
        print(f"{tall} er ikke et primtall")

# Kall funksjonene og skriv ut resultatene
sum_tall = beregn_sum_liste(tall_liste)
største_tall = finn_største_tall(tall_liste)

print(f"Summen av tallene i listen er: {sum_tall}")
print(f"Det største tallet i listen er: {største_tall}")