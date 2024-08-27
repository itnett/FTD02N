python
def beregn_prosentvis_okning():
    print("Dette programmet regner ut den prosentvise økningen når et tall øker fra en verdi til en annen.")
    gammelverdi = float(input("Skriv inn det opprinnelige tallet: "))
    nyverdi = float(input("Skriv inn hva tallet er etter den prosentvise økningen: "))
    
    vekstfaktor = nyverdi / gammelverdi
    prosent = (vekstfaktor - 1) * 100
    print(f"Når et tall øker fra {gammelverdi} til {nyverdi}, er økningen på {prosent} prosent.")

beregn_prosentvis_okning()