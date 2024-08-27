python
# Leksjon 2.1: Ekte Brøk

def is_proper_fraction(numerator, denominator):
    return numerator < denominator

# Input
numerator = int(input("Skriv inn teller: "))
denominator = int(input("Skriv inn nevner: "))

# Check if proper fraction
if is_proper_fraction(numerator, denominator):
    print(f"{numerator}/{denominator} er en ekte brøk.")
else:
    print(f"{numerator}/{denominator} er ikke en ekte brøk.")