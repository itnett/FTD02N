python
# Potenser - Beregne potenser

def calculate_power(base, exponent):
    return base ** exponent

# Input
base = float(input("Skriv inn grunntall: "))
exponent = int(input("Skriv inn eksponent: "))

# Calculate and output
result = calculate_power(base, exponent)
print(f"{base}^{exponent} er: {result}")