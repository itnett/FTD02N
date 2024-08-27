python
def sjekk_positiv_negativ(tall):
    if tall > 0:
        return "Positivt"
    elif tall < 0:
        return "Negativt"
    else:
        return "Null"

print(sjekk_positiv_negativ(10))  # Utskrift: Positivt
print(sjekk_positiv_negativ(-5))  # Utskrift: Negativt
print(sjekk_positiv_negativ(0))   # Utskrift: Null