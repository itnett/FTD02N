python
# Leksjon 2.3: Trekke Sammen Brøker med Lik Nevner

def add_fractions_same_denominator(num1, denom1, num2):
    return num1 + num2, denom1

# Input
num1 = int(input("Skriv inn første teller: "))
denom1 = int(input("Skriv inn nevner (samme for begge brøker): "))
num2 = int(input("Skriv inn andre teller: "))

# Add fractions
result_numerator, result_denominator = add_fractions_same_denominator(num1, denom1, num2)
print(f"Resultat av sammenslåing: {result_numerator}/{result_denominator}")