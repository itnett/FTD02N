python
# Trinket-kode for Leksjon 3: Brøk og Prosentregning

from fractions import Fraction

# Funksjon for å forenkle en brøk
def simplify_fraction(numerator, denominator):
    fraction = Fraction(numerator, denominator)
    return fraction

# Funksjon for å konvertere prosent til brøk
def percent_to_fraction(percent):
    return Fraction(percent, 100)

# Eksempelbruk
print("Leksjon 3: Brøk og Prosentregning")
numerator = int(input("Skriv inn telleren: "))
denominator = int(input("Skriv inn nevneren: "))
print(f"Forenklet brøk av {numerator}/{denominator} er {simplify_fraction(numerator, denominator)}")

percent = float(input("Skriv inn prosentverdien: "))
print(f"{percent}% som brøk er {percent_to_fraction(percent)}")

# Illustrere brøk og prosentregning med en graf
import matplotlib.pyplot as plt

fractions = [simplify_fraction(8, 12), simplify_fraction(9, 12)]
percentages = [25, 45]
labels = ['8/12 forenklet', '9/12 forenklet', '25% som brøk', '45% som brøk']

fraction_values = [float(f) for f in fractions]
percentage_values = [percent_to_fraction(p) for p in percentages]

plt.bar(labels[:2], fraction_values, color='blue')
plt.bar(labels[2:], percentage_values, color='green')
plt.title('Brøk og Prosentregning')
plt.xlabel('Uttrykk')
plt.ylabel('Verdi')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()