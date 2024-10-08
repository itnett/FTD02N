python
# Importerer nødvendige biblioteker
import math

# Definerer en funksjon for å beregne volumet av en kule
def calculate_sphere_volume(radius):
    # Dette demonstrerer kunnskap om matematiske formler og bruk av biblioteker
    volume = 4/3 * math.pi * radius**3
    return volume

# Definerer en funksjon for å løse andregradslikninger
def solve_quadratic(a, b, c):
    # Dette demonstrerer kunnskap om matematiske formler og bruk av biblioteker
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    else:
        return None

# Kjører funksjonene og skriver ut resultatene
radius = 5
print(f"Volumet av en kule med radius {radius} er {calculate_sphere_volume(radius)} kubikkenheter.")

a, b, c = 1, -3, 2
roots = solve_quadratic(a, b, c)
if roots is not None:
    print(f"Løsningene til likningen {a}x^2 + {b}x + {c} = 0 er x = {roots[0]} og x = {roots[1]}.")
else:
    print(f"Likningen {a}x^2 + {b}x + {c} = 0 har ingen reelle løsninger.")