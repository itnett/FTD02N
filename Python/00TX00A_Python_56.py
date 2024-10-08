python
def saldo_avskrivning(innkjopsverdi, avskrivningssats, ar):
    """
    Beregner saldoavskrivning for hvert år.

    Parametere:
    innkjopsverdi (float): Innkjøpsverdi av driftsmidlet
    avskrivningssats (float): Avskrivningssats i prosent
    ar (int): Antall år

    Returnerer:
    dict: En ordbok med avskrivningsdetaljer for hvert år
    """
    verdier = {}
    bokfort_verdi = innkjopsverdi
    
    for i in range(1, ar + 1):
        avskrivning = bokfort_verdi * (avskrivningssats / 100)
        bokfort_verdi -= avskrivning
        verdier[f"År {i}"] = {
            "Bokført verdi": bokfort_verdi + avskrivning,
            "Avskrivning": avskrivning,
            "Restverdi": bokfort_verdi
        }
    
    return verdier

# Eksempel på bruk
avskrivninger = saldo_avskrivning(innkjopsverdi=300000, avskrivningssats=20, ar=5)
for ar, detaljer i avskrivninger.items():
    print(f"{ar}: {detaljer}")