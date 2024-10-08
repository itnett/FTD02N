python
def beregn_ny_verdi_flere_ganger():
    print("Dette programmet regner ut den nye verdien på et tall som skal øke eller minke med en viss prosent et visst antall ganger.")
    svar = input("Dersom tallet skal øke, skriv 'a'. Dersom tallet skal minke, skriv 'm'.")
    
    while svar not in ['a', 'm']:
        print("Du skrev inn verken 'a' eller 'm'.")
        svar = input("Dersom tallet skal øke, skriv 'a'. Dersom tallet skal minke, skriv 'm'.")
        
    tall = float(input("Skriv inn tallet som skal få en prosentvis endring: "))
    prosent = float(input("Skriv inn prosenten tallet skal endres med: "))
    n = int(input("Skriv inn hvor mange ganger tallet skal endres: "))
    
    if svar == 'a':
        vekstfaktor = 1 + prosent / 100
        endring = "øker"
    elif svar == 'm':
        vekstfaktor = 1 - prosent / 100
        endring = "minker"
    
    nytall = tall * (vekstfaktor ** n)
    print(f"Når tallet {tall} {endring} med {prosent} prosent {n} ganger, {endring} det til {nytall}.")

beregn_ny_verdi_flere_ganger()