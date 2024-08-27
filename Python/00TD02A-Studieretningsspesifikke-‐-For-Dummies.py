python
def beregn_prosent():
    heltall = float(input("Skriv inn heltallet: "))
    prosent = float(input("Skriv inn prosentandelen (f.eks. 25 for 25%): "))
    resultat = (prosent / 100) * heltall
    print(f"{prosent}% av {heltall} er: {resultat}")