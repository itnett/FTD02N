python
# Trinket-kode for Leksjon 6.3: Sette Tall inn i Uttrykk

def sett_tall_inn_i_uttrykk(uttrykk, variabel, verdi):
    return eval(uttrykk.replace(variabel, str(verdi)))

# Eksempelbruk
print("Leksjon 6.3: Sette Tall inn i Uttrykk")
uttrykk = input("Skriv inn et uttrykk (f.eks. 2x + 3): ")
variabel = input("Skriv inn variabelen i uttrykket: ")
verdi = float(input(f"Skriv inn verdien av {variabel}: "))
resultat = sett_tall_inn_i_uttrykk(uttrykk, variabel, verdi)
print(f"Resultatet av {uttrykk} når {variabel} = {verdi} er {resultat}")