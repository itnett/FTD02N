python
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