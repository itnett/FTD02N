python
def lineaer_avskrivning(innkjopsverdi, levetid):
    """
    Beregner årlig lineær avskrivning.

    Parametere:
    innkjopsverdi (float): Innkjøpsverdi av driftsmidlet
    levetid (int): Levetid i år

    Returnerer:
    float: Årlig avskrivning
    """
    avskrivning = innkjopsverdi / levetid
    return avskrivning

# Eksempel på bruk
avskrivning = lineaer_avskrivning(innkjopsverdi=300000, levetid=5)
print(f"Årlig avskrivning: {avskrivning}")