python
def anvend_funksjon(f, verdi):
    return f(verdi)

def kvadrat(x):
    return x * x

resultat = anvend_funksjon(kvadrat, 4)
print(resultat)  # Utdata: 16