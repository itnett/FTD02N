python
import math

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

    # Håndtering av spesielle tilfeller
    if c == 0:
        solve_without_constant_term(a, b)
    elif b == 0:
        solve_without_linear_term(a, c)
    else:
        solve_general_case(a, b, c)

def solve_without_constant_term(a, b):
    print("\nSpesielt tilfelle: Konstantleddet c er null.")
    print("Likningen kan skrives som ax^2 + bx = 0.")
    print("Vi faktoriserer ut x fra begge leddene: x(ax + b) = 0.")
    print("Ifølge nullregel må enten x = 0 eller ax + b = 0.")
    x1 = 0
    x2 = -b / a
    print(f"Løsningene er: x = {x1} og x = {x2}.")
    print("Forklaring: Ved å faktorisere ut x får vi to løsninger: x = 0 og x = -b/a.")

def solve_without_linear_term(a, c):
    print("\nSpesielt tilfelle: Førstegradsleddet b er null.")
    print("Likningen kan skrives som ax^2 + c = 0.")
    print("Vi flytter c til høyre side og får: ax^2 = -c.")
    if -c / a < 0:
        print("Ingen reell løsning (vi kan ikke ta kvadratroten av et negativt tall).")
    else:
        x1 = math.sqrt(-c / a)
        x2 = -math.sqrt(-c / a)
        print(f"Løsningene er: x = {x1} og x = {x2}.")
        print("Forklaring: Vi isolerer x^2 på venstre side og tar kvadratroten av begge sider.")

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
    else:
        print("\nDiskriminanten er negativ. Likningen har ingen reelle løsninger.")
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"De komplekse løsningene er: x1 = {real_part} + {imaginary_part}i og x2 = {real_part} - {imaginary_part}i.")
        print("Forklaring: Vi har brukt ABC-formelen, hvor diskriminanten er negativ og gir komplekse røtter.")

# Kjøring av skriptet
solve_quadratic()