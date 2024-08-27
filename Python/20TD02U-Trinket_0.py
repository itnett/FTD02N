python
import math

def solve_quadratic(a, b, c):
    # Beregn diskriminanten
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Ingen reelle røtter"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"En reell rot: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"To reelle røtter: x1 = {x1}, x2 = {x2}"

# Eksempel på bruk
a = 1
b = -3
c = 2
resultat = solve_quadratic(a, b, c)
print(resultat)  # Forventet resultat: To reelle røtter: x1 = 2.0, x2 = 1.0