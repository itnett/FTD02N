python
# Algebra - Løse lineære likninger
# Løser likningen ax + b = 0

def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Uendelig mange løsninger"
        else:
            return "Ingen løsning"
    else:
        return -b / a

# Input
a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))

# Solve and output
solution = solve_linear_equation(a, b)
print("Løsningen på likningen er:", solution)