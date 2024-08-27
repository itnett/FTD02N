python
def beregn_ny_verdi():
    print("Dette programmet regner ut den nye verdien på et tall som skal øke eller minke med en viss prosent.")
    svar = input("Dersom tallet skal øke, skriv 'a'. Dersom tallet skal minke, skriv 'm'.")
    tall = float(input("Skriv inn tallet som skal få en prosentvis endring: "))
    prosent = float(input("Skriv inn prosenten tallet skal endres med: "))

    if svar == 'a':
        vekstfaktor = 1 + prosent / 100
        endring = "øker"
    elif svar == 'm':
        vekstfaktor = 1 - prosent / 100
        endring = "minker"
    else:
        print("Ugyldig valg.")
        return

    nyverdi = tall * vekstfaktor
    print(f"Når tallet {tall} {endring} med {prosent} prosent, {endring} det til {nyverdi}.")

beregn_ny_verdi()