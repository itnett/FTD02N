python
def beregn_vekstfaktor():
    print("Dette programmet regner ut vekstfaktoren ved en økning på en bestemt prosent.")
    prosent = float(input("Skriv inn denne prosenten: "))
    vekstfaktor = 1 + prosent / 100
    print(f"Vekstfaktoren ved en økning på {prosent} prosent er {vekstfaktor}.")

beregn_vekstfaktor()