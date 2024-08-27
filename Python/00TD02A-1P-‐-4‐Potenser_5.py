python
# Leksjon 4.4: Potenser med Negativ Eksponent

def negative_exponent(base, exponent):
    return base ** exponent

# Input
base = int(input("Skriv inn grunntallet: "))
exponent = int(input("Skriv inn negativ eksponent: "))

# Calculate and display
result = negative_exponent(base, exponent)
print(f"{base}^{exponent} = {result}")