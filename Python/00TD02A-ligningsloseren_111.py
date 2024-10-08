python
def solve_quadratic(a, b, c):
    if c == 0:
        # Løsning når konstantleddet mangler
        print("Løsning når konstantleddet mangler:")
        x1 = 0
        x2 = -b / a
        return x1, x2
    elif b == 0:
        # Løsning når førstegradsleddet mangler
        print("Løsning når førstegradsleddet mangler:")
        if -c / a < 0:
            return "Ingen reell løsning"
        else:
            x1 = (c / a) ** 0.5
            x2 = -(c / a) ** 0.5
            return x1, x2
    else:
        # Løsning med ABC-formelen
        print("Løsning med ABC-formelen:")
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            return x1, x2
        elif discriminant == 0:
            x1 = -b / (2*a)
            return x1,
        else:
            return "Ingen reell løsning"

# Input-spørsmål
print("For å løse en andregradslikning, vennligst gi verdiene for a, b, og c.")
a = float(input("Hva er verdien for a? "))
b = float(input("Hva er verdien for b? "))
c = float(input("Hva er verdien for c? "))

# Løsning
løsninger = solve_quadratic(a, b, c)
print("Løsningene er:", løsninger)