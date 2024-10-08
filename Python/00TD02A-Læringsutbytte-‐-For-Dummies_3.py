python
# Likninger og Formelregning - Løse kvadratiske likninger
# Løser likningen ax^2 + bx + c = 0

import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Ingen reelle løsninger"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"En løsning: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"To løsninger: x1 = {x1}, x2 = {x2}"

# Input
a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))
c = float(input("Skriv inn c: "))

# Solve and output
solution = solve_quadratic_equation(a, b, c)
print("Løsningene på likningen er:", solution)