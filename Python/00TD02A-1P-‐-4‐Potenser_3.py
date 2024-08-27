python
# Leksjon 4.2: Potensregning uten Formler

def calculate_power_without_formula(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Input
base = int(input("Skriv inn grunntallet: "))
exponent = int(input("Skriv inn eksponenten: "))

# Calculate and display
result = calculate_power_without_formula(base, exponent)
print(f"{base}^{exponent} = {result}")