python
# Leksjon 4.10: Kvadratrot

import math

def calculate_square_root(number):
    return math.sqrt(number)

# Input
number = float(input("Skriv inn et tall: "))

# Calculate and display
result = calculate_square_root(number)
print(f"Kvadratroten av {number} er {result}")