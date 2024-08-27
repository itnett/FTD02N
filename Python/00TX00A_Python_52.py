python
def handelskalkulasjon(innkjopspris, frakt, forsikring, toll, indirekte_kostnader_prosent, fortjeneste_prosent, mva_prosent=25):
    """
    Utfører handelskalkulasjon for et produkt.

    Parametere:
    innkjopspris (float): Innkjøpspris fra leverandør
    frakt (float): Fraktkostnader
    forsikring (float): Forsikringskostnader
    toll (float): Tollkostnader
    indirekte_kostnader_prosent (float): Indirekte kostnader i prosent av inntakskost
    fortjeneste_prosent (float): Fortjeneste i prosent av selvkost
    mva_prosent (float): Merverdiavgift i prosent (standardverdi 25%)

    Returnerer:
    dict: En ordbok med kalkulasjonen
    """
    inntakskost = innkjopspris + frakt + forsikring + toll
    indirekte_kostnader = inntakskost * (indirekte_kostnader_prosent / 100)
    selvkost = inntakskost + indirekte_kostnader
    fortjeneste = selvkost * (fortjeneste_prosent / 100)
    pris_uten_mva = selvkost + fortjeneste
    pris_med_mva = pris_uten_mva * (1 + mva_prosent / 100)
    
    return {
        "Inntakskost": inntakskost,
        "Indirekte kostnader": indirekte_kostnader,
        "Selvkost": selvkost,
        "Fortjeneste": fortjeneste,
        "Pris uten mva": pris_uten_mva,
        "Pris med mva": pris_med_mva
    }

# Eksempel på bruk
resultat = handelskalkulasjon(innkjopspris=100000, frakt=5000, forsikring=2000, toll=3000, indirekte_kostnader_prosent=10, fortjeneste_prosent=20)
for k, v in resultat.items():
    print(f"{k}: {v}")