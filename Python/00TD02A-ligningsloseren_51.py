python
import math

def quadratic_solver():
    print("Velkommen! Dette programmet løser andregradslikninger.")
    print("En andregradslikning har formen ax^2 + bx + c = 0.")
    print("Vennligst gi verdiene for a, b og c for likningen du vil løse.")

    # Input fra brukeren
    a = float(input("Skriv inn konstanten a (koeffisienten for x^2): "))
    b = float(input("Skriv inn konstanten b (koeffisienten for x): "))
    c = float(input("Skriv inn konstanten c (konstantleddet): "))

    # Håndtering av spesielle tilfeller
    if a == 0:
        print("Dette er ikke en andregradslikning, da koeffisienten for x^2 er null.")
        return

    print(f"\nLøsning av likningen {a}x^2 + {b}x + {c} = 0")

    # Beregning av diskriminanten
    discriminant = b**2 - 4*a*c
    print(f"Diskriminanten er: {discriminant}")

    if discriminant > 0:
        print("\nDiskriminanten er positiv. Likningen har to reelle løsninger.")
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Løsningene er: x1 = {x1} og x2 = {x2}.")
    elif discriminant == 0:
        print("\nDiskriminanten er null. Likningen har én reell løsning.")
        x = -b / (2*a)
        print(f"Løsningen er: x = {x}.")
    else:
        print("\nDiskriminanten er negativ. Likningen har ingen reelle løsninger.")
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"De komplekse løsningene er: x1 = {real_part} + {imaginary_part}i og x2 = {real_part} - {imaginary_part}i.")

    # Håndtering av tilfeller der b eller c er 0
    if c == 0:
        print("\nSpesielt tilfelle: Konstantleddet c er null.")
        x1 = 0
        x2 = -b / a
        print(f"Løsningene er: x = {x1} og x = {x2}.")
    elif b == 0:
        print("\nSpesielt tilfelle: Førstegradsleddet b er null.")
        if -c / a < 0:
            print("Ingen reell løsning (vi kan ikke ta kvadratroten av et negativt tall).")
        else:
            x1 = math.sqrt(-c / a)
            x2 = -math.sqrt(-c / a)
            print(f"Løsningene er: x = {x1} og x = {x2}.")

# Kjøring av skriptet
quadratic_solver()