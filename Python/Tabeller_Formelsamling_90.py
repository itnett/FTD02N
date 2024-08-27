python
import sympy as sp

# Definer variabler
x = sp.symbols('x')

# Likning
likning = sp.Eq(x**2 - 4, 0)

# Løsning av likning
løsning = sp.solve(likning, x)
print(f"Løsning av likning: {løsning}")