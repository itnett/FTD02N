python
import math

def solve_quadratic(a, b, c):
    # Forklaring og prosess for løsning av andregradslikninger
    print("\nForklaring:")
    print("En andregradslikning er en likning som kan skrives på formen ax^2 + bx + c = 0.")
    print("Her er a, b og c koeffisientene. Løsningene på likningen er verdiene av x som gjør at likningen blir sann.")
    
    if c == 0:
        # Løsning når konstantleddet mangler
        print("\nLøsning når konstantleddet (c) mangler:")
        print("Likningen kan skrives som ax^2 + bx = 0.")
        print("Vi faktoriserer ut x fra begge leddene: x(ax + b) = 0.")
        print("Ifølge nullregel må enten x = 0 eller ax + b = 0.")
        x1 = 0
        x2 = -b / a
        return f"x = {x1} eller x = {x2}"
    elif b == 0:
        # Løsning når førstegradsleddet mangler
        print("\nLøsning når førstegradsleddet (b) mangler:")
        print("Likningen kan skrives som ax^2 + c = 0.")
        print("Vi flytter c til høyre side og får: ax^2 = -c.")
        if -c / a < 0:
            return "Ingen reell løsning (vi kan ikke ta kvadratroten av et negativt tall)."
        else:
            x1 = math.sqrt(-c / a)
            x2 = -math.sqrt(-c / a)
            return f"x = {x1} eller x = {x2}"
    else:
        # Løsning med ABC-formelen
        print("\nLøsning med ABC-formelen:")
        print("En generell andregradslikning kan skrives som ax^2 + bx + c = 0.")
        print("For å løse denne bruker vi ABC-formelen: x = (-b ± √(b^2 - 4ac)) / 2a.")
        print("Discriminanten Δ = b^2 - 4ac bestemmer antall løsninger:")
        print("Hvis Δ > 0, har vi to reelle løsninger.")
        print("Hvis Δ = 0, har vi én reell løsning.")
        print("Hvis Δ < 0, har vi ingen reelle løsninger.")
        
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"x = {x1} eller x = {x2} (to reelle løsninger)"
        elif discriminant == 0:
            x1 = -b / (2*a)
            return f"x = {x1} (én reell løsning)"
        else:
            return "Ingen reell løsning (discriminanten er negativ)."

# Introduksjon og input-spørsmål
print("Velkommen! Dette skriptet løser andregradslikninger og forklarer prosessen.")
print("En andregradslikning har formen ax^2 + bx + c = 0.")
print("Vennligst gi verdiene for a, b og c for likningen du vil løse.")

# Input fra brukeren
a = float(input("Hva er verdien for a (koeffisienten for x^2)? "))
b = float(input("Hva er verdien for b (koeffisienten for x)? "))
c = float(input("Hva er verdien for c (konstantleddet)? "))

# Løsning
resultat = solve_quadratic(a, b, c)
print("\nLøsningene er:", resultat)

# Eksempel og detaljert prosess (bare for en mer detaljert forklaring)
print("\nEksempel på hvordan skriptet fungerer:")
print("La oss si at vi har likningen 2x^2 - 4x - 6 = 0.")
print("a = 2, b = -4, c = -6.")
print("Bruker vi ABC-formelen, finner vi først discriminanten Δ = (-4)^2 - 4*2*(-6) = 16 + 48 = 64.")
print("Siden Δ > 0, har vi to reelle løsninger.")
print("Løsningene er: x = (4 ± √64) / 4, som gir x = 2.5 og x = -1.")