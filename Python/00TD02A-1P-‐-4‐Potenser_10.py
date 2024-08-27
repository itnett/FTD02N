python
# Leksjon 4.9: Potenser og Regnerekkefølge

def calculate_expression(expression):
    return eval(expression)

# Input
expression = input("Skriv inn en matematisk uttrykk med potenser: ")

# Calculate and display
result = calculate_expression(expression)
print(f"Resultatet av uttrykket {expression} er {result}")