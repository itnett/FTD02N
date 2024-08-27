python
def beregn_vekstfaktor():
    print("Dette programmet regner ut vekstfaktoren ved en økning på en bestemt prosent.")
    prosent = float(input("Skriv inn denne prosenten: "))
    vekstfaktor = 1 + prosent / 100
    print(f"Vekstfaktoren ved en økning på {prosent} prosent er {vekstfaktor}.")

def beregn_ny_pris():
    print("Dette programmet regner ut den nye prisen på en vare som får en prisøkning på en viss prosent.")
    gammelpris = float(input("Skriv inn nåværende pris på varen: "))
    prosent = float(input("Skriv inn prosenten for prisøkningen: "))
    vekstfaktor = 1 + prosent / 100
    nypris = gammelpris * vekstfaktor
    print(f"Når en vare som koster {gammelpris} kroner får en prisøkning på {prosent} prosent, blir den nye prisen {nypris} kroner.")

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

def beregn_ny_verdi_flere_ganger():
    print("Dette programmet regner ut den nye verdien på et tall som skal øke eller minke med en viss prosent et visst antall ganger.")
    svar = "feil"
    while svar not in ['a', 'm']:
        svar = input("Dersom tallet skal øke, skriv 'a'. Dersom tallet skal minke, skriv 'm'.")
        if svar not in ['a', 'm']:
            print("Du skrev inn verken 'a' eller 'm'.")
        
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

def beregn_prosentvis_okning():
    print("Dette programmet regner ut den prosentvise økningen når et tall øker fra en verdi til en annen.")
    gammelverdi = float(input("Skriv inn det opprinnelige tallet: "))
    nyverdi = float(input("Skriv inn hva tallet er etter den prosentvise økningen: "))
    
    vekstfaktor = nyverdi / gammelverdi
    prosent = (vekstfaktor - 1) * 100
    print(f"Når et tall øker fra {gammelverdi} til {nyverdi}, er økningen på {prosent} prosent.")

def prosentprogram():
    print("Velkommen til prosentprogrammet!")
    print("Velg en av følgende funksjoner:")
    print("1. Beregn vekstfaktor fra prosent")
    print("2. Beregn ny pris etter prosentvis økning")
    print("3. Beregn ny verdi etter prosentvis endring (økning eller minking)")
    print("4. Beregn ny verdi etter flere prosentvise endringer")
    print("5. Beregn prosentvis endring basert på opprinnelig og ny verdi")
    
    valg = input("Skriv inn nummeret på funksjonen du vil bruke: ")
    
    if valg == '1':
        beregn_vekstfaktor()
    elif valg == '2':
        beregn_ny_pris()
    elif valg == '3':
        beregn_ny_verdi()
    elif valg == '4':
        beregn_ny_verdi_flere_ganger()
    elif valg == '5':
        beregn_prosentvis_okning()
    else:
        print("Ugyldig valg. Vennligst prøv igjen.")

prosentprogram()