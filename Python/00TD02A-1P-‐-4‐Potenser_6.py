python
# Leksjon 4.5: Potenser med 10 som Grunntall

def power_of_10(exponent):
    return 10 ** exponent

# Input
exponent = int(input("Skriv inn eksponenten: "))

# Calculate and display
result = power_of_10(exponent)
print(f"10^{exponent} = {result}")