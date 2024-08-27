python
# Leksjon 4.3: Potensregning

def multiply_powers(base, exp1, exp2):
    return base ** (exp1 + exp2)

def divide_powers(base, exp1, exp2):
    return base ** (exp1 - exp2)

def power_of_power(base, exp1, exp2):
    return base ** (exp1 * exp2)

# Input
base = int(input("Skriv inn grunntallet: "))
exp1 = int(input("Skriv inn første eksponent: "))
exp2 = int(input("Skriv inn andre eksponent: "))

# Calculate and display
mult_result = multiply_powers(base, exp1, exp2)
div_result = divide_powers(base, exp1, exp2)
pow_result = power_of_power(base, exp1, exp2)
print(f"{base}^{exp1} * {base}^{exp2} = {base}^{exp1 + exp2} = {mult_result}")
print(f"{base}^{exp1} / {base}^{exp2} = {base}^{exp1 - exp2} = {div_result}")
print(f"({base}^{exp1})^{exp2} = {base}^{exp1 * exp2} = {pow_result}")