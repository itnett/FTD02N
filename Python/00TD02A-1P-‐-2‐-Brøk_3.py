python
# Leksjon 2.4: Trekke Sammen Brøker med Ulik Nevner

def find_lcm(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return abs(a * b) // gcd(a, b)

def add_fractions_diff_denominators(num1, denom1, num2, denom2):
    lcm = find_lcm(denom1, denom2)
    num1 = num1 * (lcm // denom1)
    num2 = num2 * (lcm // denom2)
    return num1 + num2, lcm

# Input
num1 = int(input("Skriv inn første teller: "))
denom1 = int(input("Skriv inn første nevner: "))
num2 = int(input("Skriv inn andre teller: "))
denom2 = int(input("Skriv inn andre nevner: "))

# Add fractions
result_numerator, result_denominator = add_fractions_diff_denominators(num1, denom1, num2, denom2)
print(f"Resultat av sammenslåing: {result_numerator}/{result_denominator}")