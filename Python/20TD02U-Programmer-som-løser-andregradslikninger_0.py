python
import math

def solve_quadratic():
    print("Dette programmet løser andregradslikningen ax^2 + bx + c = 0.")
    
    a = float(input("Skriv inn konstanten a: "))
    b = float(input("Skriv inn konstanten b: "))
    c = float(input("Skriv inn konstanten c: "))
    
    D = b**2 - 4*a*c
    
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Løsningene er x1 = {x1} og x2 = {x2}.")
    elif D == 0:
        x1 = x2 = -b / (2*a)
        print(f"Løsningen er x1 = x2 = {x1}.")
    else:
        print("Ingen reelle løsninger.")

solve_quadratic()