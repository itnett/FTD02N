python
import math

def quadratic_solver():
    print("Velkommen! Dette programmet hjelper deg med å løse andregradslikninger.")
    print("En andregradslikning har formen ax^2 + bx + c = 0.")
    print("Vennligst gi verdiene for a, b og c for likningen du vil løse.")

    # Input fra brukeren
    a = float(input("Hva er verdien for a (koeffisienten for x^2)? "))
    b = float(input("Hva er verdien for b (koeffisienten for x)? "))
    c = float(input("Hva er verdien for c (konstantleddet)? "))

    # Håndtering av spesielle tilfeller
    if a == 0:
        print("Dette er ikke en andregradslikning, da koeffisienten for x^2 er null.")
        return

    print("\nAnalyse av likningen:")
    if c == 0:
        print("\nLøsning når konstantleddet (c) mangler:")
        print("Likningen kan skrives som ax^2 + bx = 0.")
        print("Vi faktoriserer ut x fra begge leddene: x(ax + b) = 0.")
        print("Ifølge nullregelen må enten x = 0 eller ax + b = 0.")
        x1 = 0
        x2 = -b / a
        print(f"Løsningene er: x = {x1} og x = {x2}.")
        return

    elif b == 0:
        print("\nLøsning når førstegradsleddet (b) mangler:")
        print("Likningen kan skrives som ax^2 + c = 0.")
        print("Vi flytter c til høyre side og får: ax^2 = -c.")
        if -c / a < 0:
            print("Ingen reell løsning (vi kan ikke ta kvadratroten av et negativt tall).")
            return
        else:
            x1 = math.sqrt(-c / a)
            x2 = -math.sqrt(-c / a)
            print(f"Løsningene er: x = {x1} og x = {x2}.")
            return

    else:
        # Beregning av diskriminanten
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            print("\nLøsning ved bruk av abc-formelen:")
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Løsningene er: x = {x1} og x = {x2}.")
            return

        elif discriminant == 0:
            print("\nLøsning når diskriminanten er null:")
            x = -b / (2*a)
            print(f"Løsningen er: x = {x}.")
            return

        else:
            print("\nIngen reell løsning (diskriminanten er negativ).")
            print("For å få en kompleks løsning, bruk komplekse tall:")
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(-discriminant) / (2*a)
            print(f"De komplekse løsningene er: x = {real_part} + {imaginary_part}i og x = {real_part} - {imaginary_part}i.")
            return

# Kjøring av skriptet
quadratic_solver()