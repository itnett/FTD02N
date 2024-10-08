python
from sympy import exp, sqrt, pi, oo, integrate, Symbol

x = Symbol('x')
normalfordeling = exp(-x**2 / 2) / sqrt(2 * pi)

# Beregn sannsynligheten for at en standard normalfordelt variabel er mellom -1 og 1
sannsynlighet = integrate(normalfordeling, (x, -1, 1))
print(f"Sannsynlighet: {sannsynlighet.evalf()}")  # Output: Sannsynlighet: 0.682689492137086