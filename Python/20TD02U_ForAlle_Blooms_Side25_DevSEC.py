python
# Validering av tall
def er_gyldig_tall(verdi):
    return verdi.isdigit()

tall = input("Skriv inn et tall: ")
if er_gyldig_tall(tall):
    tall = int(tall)
else:
    print("Ugyldig tall!")