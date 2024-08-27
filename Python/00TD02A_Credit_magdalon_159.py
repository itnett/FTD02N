python
from sympy import symbols, integrate, S

t = symbols('t')  # Tid
responstid_funksjon = 0.1 * t**2 + 5 * t + 10  # Simulert responstid som funksjon av tid

# Beregn gjennomsnittlig responstid over 10 sekunder
gjennomsnittlig_responstid = integrate(responstid_funksjon, (t, 0, 10)) / 10
print(f"Gjennomsnittlig responstid: {gjennomsnittlig_responstid}")