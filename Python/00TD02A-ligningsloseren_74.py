python
import math

def solve_quadratic():
    # Introduksjon og input-spørsmål
    print("Velkommen! Dette skriptet hjelper deg med å løse andregradslikninger uten bruk av abc-formelen.")
    print("En andregradslikning har formen ax^2 + bx + c = 0.")
    print("Vennligst gi verdiene for a, b og c for likningen du vil løse.")

    # Input fra brukeren
    a = float(input("Hva er verdien for a (koeffisienten for x^2)? "))
    b = float(input("Hva er verdien for b (koeffisienten for x)? "))
    c = float(input("Hva er verdien for c (konstantleddet)? "))

    # Ingen konstantledd (c = 0)
    if c == 0:
        print("\nLøsning når konstantleddet (c) mangler:")
        print("Likningen kan skrives som ax^2 + bx = 0.")
        print("Vi faktoriserer ut x fra begge leddene: x(ax + b) = 0.")
        print("Ifølge nullregelen må enten x = 0 eller ax + b = 0.")
        x1 = 0
        x2 = -b / a
        return f"Løsningene er: x = {x1} og x = {x2}."
    
    # Ingen førstegradsledd (b = 0)
    elif b == 0:
        print("\nLøsning når førstegradsleddet (b) mangler:")
        print("Likningen kan skrives som ax^2 + c = 0.")
        print("Vi flytter c til høyre side og får: ax^2 = -c.")
        if -c / a < 0:
            return "Ingen reell løsning (vi kan ikke ta kvadratroten av et negativt tall)."
        else:
            x1 = math.sqrt(-c / a)
            x2 = -math.sqrt(-c / a)
            return f"Løsningene er: x = {x1} og x = {x2}."
    
    # Faktorisering og fullstendige kvadrater
    else:
        print("\nForsøk på å løse ved faktorisering og fullstendige kvadrater:")
        
        # Fullstendige kvadrater
        if (b**2 - 4*a*c) >= 0:
            print("Løsning ved fullstendige kvadrater:")
            h = b / (2*a)
            k = c / a - (h**2)
            if k >= 0:
                x1 = -h + math.sqrt(k)
                x2 = -h - math.sqrt(k)
                return f"Løsningene er: x = {x1} og x = {x2}."
            else:
                print("Ingen reell løsning med fullstendige kvadrater.")
        
        # Faktorisering (eksempel med stirremetoden)
        print("Forsøk på å løse ved faktorisering (stirremetoden):")
        for i in range(int(-c/a) - 1, int(c/a) + 1):
            if i != 0 and (c / i) + i == b:
                x1 = i
                x2 = -c / i
                return f"Løsningene er: x = {x1} og x = {x2}."
        
        return "Kunne ikke løse ved faktorisering eller fullstendige kvadrater."

# Kjøring av skriptet
print(solve_quadratic())