python
ordinært_resultat_før_skatt = 200000
rentekostnader = 50000
totalkapital = 1000000
egenkapital = 600000

totalkapitalrentabilitet = ((ordinært_resultat_før_skatt + rentekostnader) / totalkapital) * 100
egenkapitalrentabilitet = (ordinært_resultat_før_skatt / egenkapital) * 100

print(f"Totalkapitalrentabilitet: {totalkapitalrentabilitet:.2f}%")
print(f"Egenkapitalrentabilitet: {egenkapitalrentabilitet:.2f}%")