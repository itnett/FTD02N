python
import math

def solve_quadratic():
    print("Dette programmet løser andregradslikningen ax^2 + bx + c = 0.")
    
    a = float(input("Skriv inn konstanten a: "))
    b = float(input("Skriv inn konstanten b: "))
    c = float(input("Skriv inn konstanten c: "))
    
    if a == 0:
        if b != 0:
            x = -c / b
            print(f"Løsningen er x = {x}.")
        else:
            print("Dette er ikke en gyldig likning.")
        return
    
    D = b**2 - 4*a*c
    
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Løsningene er x1 = {x1} og x2 = {x2}.")
    elif D == 0:
        x1 = x2 = -b / (2*a)
        print(f"Løsningen er x1 = x2 = {x1}.")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        print(f"Løsningene er x1 = {real_part} + {imaginary_part}i og x2 = {real_part} - {imaginary_part}i.")

solve_quadratic()