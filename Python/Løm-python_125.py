python
def beregn_ebitda(driftsresultat, avskrivninger, amortiseringer):
    ebitda = driftsresultat + avskrivninger + amortiseringer
    return ebitda

driftsresultat = 100000
avskrivninger = 20000
amortiseringer = 10000
ebitda = beregn_ebitda(driftsresultat, avskrivninger, amortiseringer)
print(f"EBITDA: {ebitda}")