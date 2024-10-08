python
# Leksjon 3.2: Prosent som Brøk

def percent_to_fraction(percent):
    numerator = percent
    denominator = 100
    return numerator, denominator

def simplify_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Input
percent = int(input("Skriv inn en prosentverdi: "))

# Convert to fraction
numerator, denominator = percent_to_fraction(percent)
simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
print(f"{percent}% som brøk er: {numerator}/{denominator} som kan forenkles til {simplified_numerator}/{simplified_denominator}")