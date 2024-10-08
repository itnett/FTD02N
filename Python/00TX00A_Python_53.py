python
def bruttofortjeneste(salgspris, inntakskost):
    """
    Beregner bruttofortjeneste i kroner og prosent.

    Parametere:
    salgspris (float): Salgspris ekskl. mva
    inntakskost (float): Inntakskost

    Returnerer:
    dict: En ordbok med bruttofortjeneste
    """
    bruttofortjeneste_kroner = salgspris - inntakskost
    bruttofortjeneste_prosent = (bruttofortjeneste_kroner / salgspris) * 100
    avanse_prosent = (bruttofortjeneste_kroner / inntakskost) * 100
    
    return {
        "Bruttofortjeneste i kroner": bruttofortjeneste_kroner,
        "Bruttofortjeneste i prosent": bruttofortjeneste_prosent,
        "Avanse i prosent": avanse_prosent
    }

# Eksempel på bruk
resultat = bruttofortjeneste(salgspris=100352, inntakskost=64000)
for k, v in resultat.items():
    print(f"{k}: {v}")