python
# Leksjon 4.1: Potenser

def calculate_power(base, exponent):
    return base ** exponent

# Input
base = int(input("Skriv inn grunntallet: "))
exponent = int(input("Skriv inn eksponenten: "))

# Calculate and display
result = calculate_power(base, exponent)
print(f"{base}^{exponent} = {result}")