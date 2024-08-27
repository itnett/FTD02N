python
alder = input("Skriv inn alderen din: ")
try:
    alder = int(alder)
    if alder < 0:
        raise ValueError("Alder kan ikke være negativ.")
except ValueError:
    print("Ugyldig alder. Vennligst skriv inn et positivt heltall.")