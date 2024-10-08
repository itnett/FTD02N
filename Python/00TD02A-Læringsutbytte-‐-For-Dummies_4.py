python
# Trigonometri og Geometri - Pytagoras' setning
# Beregner hypotenusen i en rettvinklet trekant

import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Input
a = float(input("Skriv inn lengden av den ene kateten: "))
b = float(input("Skriv inn lengden av den andre kateten: "))

# Calculate and output
hypotenuse = calculate_hypotenuse(a, b)
print(f"Hypotenusen er: {hypotenuse:.2f}")