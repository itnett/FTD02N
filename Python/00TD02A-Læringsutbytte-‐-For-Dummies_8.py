python
# Studieretningsspesifikke Temaer - Logaritmer
# Beregner logaritmen til et tall

import math

def calculate_logarithm(base, value):
    return math.log(value, base)

# Input
base = float(input("Skriv inn grunntall: "))
value = float(input("Skriv inn verdien: "))

# Calculate and output
logarithm = calculate_logarithm(base, value)
print(f"Logaritmen av {value} med grunntall {base} er: {logarithm}")