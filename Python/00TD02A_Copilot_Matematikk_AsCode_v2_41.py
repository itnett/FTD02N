python
import sympy as sp

# Definere variabel og funksjon
x = sp.symbols('x')
f = x**3 + 2*x**2 + 3*x + 4

# Derivere funksjonen
f_prime = sp.diff(f, x)
f_prime