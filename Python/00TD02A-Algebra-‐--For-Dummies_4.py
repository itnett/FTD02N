python
# Trinket-kode for Leksjon 5: Tall på standardform

# Funksjon for å konvertere til standardform
def to_standard_form(number):
    return "{:.2e}".format(number)

# Eksempelbruk
print("Leksjon 5: Tall på standardform")
number = float(input("Skriv inn tallet: "))
print(f"{number} i standardform er {to_standard_form(number)}")

# Illustrere standardform med en graf
import matplotlib.pyplot as plt
import numpy as np

numbers = [72000, 0.00056, 4500000]
standard_forms = [to_standard_form(num) for num in numbers]

plt.bar([str(num) for num in numbers], [float(f.split('e')[0]) for f in standard_forms], color='orange')
plt.title('Tall på standardform')
plt.xlabel('Tallet')
plt.ylabel('Standardform')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()