python
# Leksjon 4.7: Små Tall på Standardform

def small_number_to_scientific_notation(number):
    exponent = 0
    while number < 1:
        number *= 10
        exponent -= 1
    return number, exponent

# Input
number = float(input("Skriv inn et lite tall: "))

# Calculate and display
coefficient, exponent = small_number_to_scientific_notation(number)
print(f"{number} i standardform er {coefficient} * 10^{exponent}")