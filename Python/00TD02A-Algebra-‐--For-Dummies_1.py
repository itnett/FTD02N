python
# Trinket-kode for Leksjon 2: Regneregler

# Funksjoner for de ulike regnereglene
def parenteser():
    return (3 + 2) * 4

def eksponenter():
    return 2 ** 3

def multiplikasjon_og_divisjon():
    return 6 / 2 * 3

def addisjon_og_subtraksjon():
    return 7 - 2 + 5

# Eksempelbruk
print("Leksjon 2: Regneregler")
print(f"Parenteser: (3 + 2) * 4 = {parenteser()}")
print(f"Eksponenter: 2^3 = {eksponenter()}")
print(f"Multiplikasjon og divisjon: 6 / 2 * 3 = {multiplikasjon_og_divisjon()}")
print(f"Addisjon og subtraksjon: 7 - 2 + 5 = {addisjon_og_subtraksjon()}")

# Illustrere regneregler med en graf
import matplotlib.pyplot as plt
import numpy as np

operations = ['Parenteser', 'Eksponenter', 'Multiplikasjon/Divisjon', 'Addisjon/Subtraksjon']
values = [parenteser(), eksponenter(), multiplikasjon_og_divisjon(), addisjon_og_subtraksjon()]

plt.bar(operations, values, color=['blue', 'green', 'red', 'purple'])
plt.title('Resultater av forskjellige regneregler')
plt.xlabel('Regel')
plt.ylabel('Resultat')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()