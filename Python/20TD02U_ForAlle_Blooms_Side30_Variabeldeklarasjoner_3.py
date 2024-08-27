python
# Funksjon som beregner summen av to tall
def beregn_sum(a, b):
    return a + b

# Funksjon som sjekker om et tall er et primtall
def er_primer(tall):
    if tall < 2:
        return False
    for i in range(2, int(tall ** 0.5) + 1):
        if tall % i == 0:
            return False
    return True

# Funksjon som finner det største tallet i en liste
def finn_største(liste):
    største = liste[0]
    for tall i liste:
        if tall > største:
            største = tall
    return største

# Bruk av funksjonene
print(beregn_sum(5, 7))             # Output: 12
print(er_primer(17))                # Output: True
print(finn_største([10, 20, 30]))   # Output: 30