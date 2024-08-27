python
# Leksjon 4.6: Store Tall på Standardform

def large_number_to_scientific_notation(number):
    exponent = 0
    while number >= 10:
        number /= 10
        exponent += 1
    return number, exponent

# Input
number = float(input("Skriv inn et stort tall: "))

# Calculate and display
coefficient, exponent = large_number_to_scientific_notation(number)
print(f"{number} i standardform er {coefficient} * 10^{exponent}")