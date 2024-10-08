python
# Definer alkoholmengde og personinformasjon
alkohol = {"Trine": 0, "Truls": 0, "Kari": 0, "Tormod": 1}  # i liter
personer = {"Trine": 50, "Truls": 70, "Kari": 60, "Tormod": 80}  # i kg

# Widmark formel for promilleberegning
def beregn_promille(alkohol, vekt, reduksjonsfaktor):
    return (alkohol * 1000) / (reduksjonsfaktor * vekt)

# Beregn promille for hver person
for person, mengde in alkohol.items():
    vekt = personer[person]
    reduksjonsfaktor = 0.7 if person in ["Truls", "Tormod"] else 0.6
    promille = beregn_promille(mengde, vekt, reduksjonsfaktor)
    print(f"{person} har promille: {promille:.2f}")