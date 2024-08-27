python
# Trinket-kode for Leksjon 6.4: Trekke Sammen Ledd

def trekk_sammen_ledd(uttrykk):
    ledd = uttrykk.split(' ')
    samlet = {}
    for ledd in ledd:
        if ledd[-1].isalpha():
            variabel = ledd[-1]
            koeff = int(ledd[:-1])
        else:
            variabel = ''
            koeff = int(ledd)
        if variabel in samlet:
            samlet[variabel] += koeff
        else:
            samlet[variabel] = koeff
    return ' + '.join([f"{samlet[v]}{v}" for v in samlet])

# Eksempelbruk
print("Leksjon 6.4: Trekke Sammen Ledd")
uttrykk = input("Skriv inn et uttrykk med ledd (f.eks. 4a + 3a): ")
resultat = trekk_sammen_ledd(uttrykk)
print(f"Resultatet av sammentrekning: {resultat}")