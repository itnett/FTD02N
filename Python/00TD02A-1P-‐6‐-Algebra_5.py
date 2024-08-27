python
# Trinket-kode for Leksjon 6.6: Multiplisere inn i en Parentes

def multiplisere_inn_parentes(koeffisient, uttrykk):
    ledd = uttrykk.split(' ')
    resultat = []
    for ledd in ledd:
        if ledd[-1].isalpha():
            variabel = ledd[-1]
            resultat.append(f"{koeffisient * int(ledd[:-1])}{variabel}")
        else:
            resultat.append(f"{koeffisient * int(ledd)}")
    return ' + '.join(resultat)

# Eksempelbruk
print("Leksjon 6.6: Multiplisere inn i en Parentes")
koeffisient = int(input("Skriv inn koeffisienten: "))
uttrykk = input("Skriv inn uttrykket inne i parentes (f.eks. y + 5): ")
resultat = multiplisere_inn_parentes(koeffisient, uttrykk)
print(f"Resultatet av {koeffisient}({uttrykk}) er {resultat}")