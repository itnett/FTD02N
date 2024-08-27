python
from sympy import symbols, lambdify

brukere, responstid = symbols('brukere responstid')
responstid_funksjon = 0.1 * brukere**2 + 5 * brukere + 10  # Simulert responstid som funksjon av antall brukere

# Konverter til Python-funksjon for numerisk evaluering
responstid_lambda = lambdify(brukere, responstid_funksjon)

# Beregn responstid for 100 brukere
responstid_100 = responstid_lambda(100)
print(f"Responstid for 100 brukere: {responstid_100} ms")