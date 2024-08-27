python
# Trinket-kode for Leksjon 6: Sammentrekning og Faktorisering

# Funksjon for å forenkle uttrykk ved sammentrekning
def simplify_expression(expression):
    return eval(expression)

# Funksjon for å faktorisere uttrykk (eksempel)
def factor_expression(expression):
    # Denne funksjonen faktorisering er en forenkling
    # For avansert faktorisering kan sympy biblioteket brukes
    from sympy import symbols, factor
    x = symbols('x')
    return factor(expression)

# Eksempelbruk
print("Leksjon 6: Sammentrekning og Faktorisering")
expression = input("Skriv inn uttrykket for sammentrekning (f.eks. '4+3-2'): ")
print(f"Forenklet uttrykk: {simplify_expression(expression)}")

factor_expr = input("Skriv inn uttrykket for faktorisering (f.eks. 'x**2 - 4'): ")
print(f"Faktoriser uttrykk: {factor_expression(factor_expr)}")

# Illustrere sammentrekning og faktorisering med en graf
import matplotlib.pyplot as plt
import numpy as np

expressions = ['4a + 5a - 2a', 'x**2 - 4', '3*(a + 4)']
simplified_values = [simplify_expression('4+5-2'), 'x**2 - 4', '3*(a + 4)']

plt.bar(expressions, simplified_values, color='purple')
plt.title('Sammentrekning og Faktorisering')
plt.xlabel('Uttrykk')
plt.ylabel('Resultat')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.show()