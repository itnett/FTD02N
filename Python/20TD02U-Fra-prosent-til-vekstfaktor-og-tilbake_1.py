python
def beregn_ny_pris():
    print("Dette programmet regner ut den nye prisen på en vare som får en prisøkning på en viss prosent.")
    gammelpris = float(input("Skriv inn nåværende pris på varen: "))
    prosent = float(input("Skriv inn prosenten for prisøkningen: "))
    vekstfaktor = 1 + prosent / 100
    nypris = gammelpris * vekstfaktor
    print(f"Når en vare som koster {gammelpris} kroner får en prisøkning på {prosent} prosent, blir den nye prisen {nypris} kroner.")

beregn_ny_pris()