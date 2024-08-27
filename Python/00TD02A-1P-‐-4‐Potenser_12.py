python
# Leksjon 4.11: Regning med Kvadratrøtter

def multiply_square_roots(a, b):
    return math.sqrt(a * b)

def divide_square_roots(a, b):
    return math.sqrt(a / b)

# Input
a = float(input("Skriv inn første tall: "))
b = float(input("Skriv inn andre tall: "))

# Calculate and display
mult_result = multiply_square_roots(a, b)
div_result = divide_square_roots(a, b)
print(f"Kvadratroten av {a} * {b} er {mult_result}")
print(f"Kvadratroten av {a} / {b} er {div_result}")