python
def beregn_lonnskostnader(bruttolonn, skattetrekk_prosent, arbeidsgiveravgift_prosent, feriepenger_prosent):
    """
    Beregner totale lønnskostnader for arbeidsgiver.

    Parametere:
    bruttolonn (float): Brutto lønn
    skattetrekk_prosent (float): Skattetrekk i prosent
    arbeidsgiveravgift_prosent (float): Arbeidsgiveravgift i prosent
    feriepenger_prosent (float): Feriepenger i prosent

    Returnerer:
    dict: En ordbok med lønnskostnader
    """
    skattetrekk = bruttolonn * (skattetrekk_prosent / 100)
    arbeidsgiveravgift = bruttolonn * (arbeidsgiveravgift_prosent / 100)
    feriepenger = bruttolonn * (feriepenger_prosent / 100)
    arbeidsgiveravgift_feriepenger = feriepenger * (arbeidsgiveravgift_prosent / 100)
    total_lonn = bruttolonn - skattetrekk + arbeidsgiveravgift + feriepenger + arbeidsgiveravgift_feriepenger
    
    return {
        "Skattetrekk": skattetrekk,
        "Arbeidsgiveravgift": arbeidsgiveravgift,
        "Feriepenger": feriepenger,
        "Arbeidsgiveravgift på feriepenger": arbeidsgiveravgift_feriepenger,
        "Total lønn": total_lonn
    }

# Eksempel på bruk
resultat = beregn_lonnskostnader(bruttolonn=40000, skattetrekk_prosent=30, arbeidsgiveravgift_prosent=14.1, feriepenger_prosent=12)
for k, v in resultat.items():
    print(f"{k}: {v}")