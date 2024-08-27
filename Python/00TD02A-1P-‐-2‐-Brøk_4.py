python
# Leksjon 2.5: Multiplikasjon av Brøk

def multiply_fractions(num1, denom1, num2, denom2):
    return num1 * num2, denom1 * denom2

# Input
num1 = int(input("Skriv inn første teller: "))
denom1 = int(input("Skriv inn første nevner: "))
num2 = int(input("Skriv inn andre teller: "))
denom2 = int(input("Skriv inn andre nevner: "))

# Multiply fractions
result_numerator, result_denominator = multiply_fractions(num1, denom1, num2, denom2)
print(f"Resultat av multiplikasjon: {result_numerator}/{result_denominator}")