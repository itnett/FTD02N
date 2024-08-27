python
# Leksjon 4.8: Regning med Tall på Standardform

def multiply_scientific_notation(a, b, exp1, exp2):
    coefficient = a * b
    exponent = exp1 + exp2
    return coefficient, exponent

def divide_scientific_notation(a, b, exp1, exp2):
    coefficient = a / b
    exponent = exp1 - exp2
    return coefficient, exponent

# Input
a = float(input("Skriv inn første koeffisient: "))
exp1 = int(input("Skriv inn første eksponent: "))
b = float(input("Skriv inn andre koeffisient: "))
exp2 = int(input("Skriv inn andre eksponent: "))

# Calculate and display
mult_coefficient, mult_exponent = multiply_scientific_notation(a, b, exp1, exp2)
div_coefficient, div_exponent = divide_scientific_notation(a, b, exp1, exp2)
print(f"({a} * 10^{exp1}) * ({b} * 10^{exp2}) = {mult_coefficient} * 10^{mult_exponent}")
print(f"({a} * 10^{exp1}) / ({b} * 10^{exp2}) = {div_coefficient} * 10^{div_exponent}")