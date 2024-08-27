python
# Leksjon 2.2: Utviding og Forkorting av Brøk

def expand_fraction(numerator, denominator, factor):
    return numerator * factor, denominator * factor

def reduce_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

# Input
numerator = int(input("Skriv inn teller: "))
denominator = int(input("Skriv inn nevner: "))
factor = int(input("Skriv inn utvidingsfaktor: "))

# Expand fraction
expanded_numerator, expanded_denominator = expand_fraction(numerator, denominator, factor)
print(f"Utvidet brøk: {expanded_numerator}/{expanded_denominator}")

# Reduce fraction
reduced_numerator, reduced_denominator = reduce_fraction(numerator, denominator)
print(f"Forkortet brøk: {reduced_numerator}/{reduced_denominator}")