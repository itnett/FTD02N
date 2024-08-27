python
import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def solve_quadratic():
    print("Velkommen! Dette programmet løser andregradslikninger og forklarer prosessen.")
    print("En andregradslikning har formen ax^2 + bx + c = 0.")
    print("Vennligst gi verdiene for a, b og c for likningen du vil løse.")
    
    # Input fra brukeren
    a = float(input("Skriv inn konstanten a (koeffisienten for x^2): "))
    b = float(input("Skriv inn konstanten b (koeffisienten for x): "))
    c = float(input("Skriv inn konstanten c (konstantleddet): "))
    
    if a == 0:
        print("Dette er ikke en andregradslikning, da koeffisienten for x^2 er null.")
        return

    print(f"\nLøsning av likningen {a}x^2 + {b}x + {c} = 0")
    
    # Definerer symbolet x
    x = sp.Symbol('x')
    
    # Lager likningen med SymPy
    equation = sp.Eq(a*x**2 + b*x + c, 0)
    print(f"Ligningen som skal løses: {equation}")
    
    # Løser likningen
    solutions = sp.solveset(equation, x, domain=sp.S.Reals)
    print(f"Løsningene for ligningen er: {solutions}")

    # Håndtering av spesielle tilfeller
    if c == 0:
        x1, x2 = solve_without_constant_term(a, b)
    elif b == 0:
        x1, x2 = solve_without_linear_term(a, c)
    else:
        x1, x2 = solve_general_case(a, b, c)

    # Plotting av funksjonen
    plot_function(a, b, c, solutions)

def solve_without_constant_term(a, b):
    print("\nSpesielt tilfelle: Konstantleddet c er null.")
    print("Likningen kan skrives som ax^2 + bx = 0.")
    print("Vi faktoriserer ut x fra begge leddene: x(ax + b) = 0.")
    print("Ifølge nullregel må enten x = 0 eller ax + b = 0.")
    x1 = 0
    x2 = -b / a
    print(f"Løsningene er: x = {x1} og x = {x2}.")
    print("Forklaring: Ved å faktorisere ut x får vi to løsninger: x = 0 og x = -b/a.")
    return x1, x2

def solve_without_linear_term(a, c):
    print("\nSpesielt tilfelle: Førstegradsleddet b er null.")
    print("Likningen kan skrives som ax^2 + c = 0.")
    print("Vi flytter c til høyre side og får: ax^2 = -c.")
    if -c / a < 0:
        print("Ingen reell løsning (vi kan ikke ta kvadratroten av et negativt tall).")
        return None, None
    else:
        x1 = math.sqrt(-c / a)
        x2 = -math.sqrt(-c / a)
        print(f"Løsningene er: x = {x1} og x = {x2}.")
        print("Forklaring: Vi isolerer x^2 på venstre side og tar kvadratroten av begge sider.")
        return x1, x2

def solve_general_case(a, b, c):
    discriminant = b**2 - 4*a*c
    print(f"Diskriminanten er: {discriminant}")

    if discriminant > 0:
        print("\nDiskriminanten er positiv. Likningen har to reelle løsninger.")
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Løsningene er: x1 = {x1} og x2 = {x2}.")
        print("Forklaring: Vi har brukt ABC-formelen, hvor diskriminanten er positiv og gir to reelle røtter.")
    elif discriminant == 0:
        print("\nDiskriminanten er null. Likningen har én reell løsning.")
        x = -b / (2*a)
        print(f"Løsningen er: x = {x}.")
        print("Forklaring: Vi har brukt ABC-formelen, hvor diskriminanten er null og gir én dobbel rot.")
        return x, x
    else:
        print("\nDiskriminanten er negativ. Likningen har ingen reelle løsninger.")
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"De komplekse løsningene er: x1 = {real_part} + {imaginary_part}i og x2 = {real_part} - {imaginary_part}i.")
        print("Forklaring: Vi har brukt ABC-formelen, hvor diskriminanten er negativ og gir komplekse røtter.")
        return None, None

    return x1, x2

def plot_function(a, b, c, solutions):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a*x_vals**2 + b*x_vals + c
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'{a}x^2 + {b}x + {c} = 0')
    
    for sol in solutions:
        if sol.is_real:
            plt.plot(float(sol), 0, 'ro') # Markerer reelle løsninger
            plt.annotate(f'x = {sol}', xy=(float(sol), 0), xytext=(float(sol), 5), textcoords='offset points')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title("Grafisk løsning av andregradslikningen")
    plt.legend()
    plt.show()

# Kjøring av skriptet
solve_quadratic()