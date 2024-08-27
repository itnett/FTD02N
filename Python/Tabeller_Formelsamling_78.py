python
import sympy as sp

# Define symbols for latent heat (L), mass (m)
L, m = sp.symbols('L m')

# Heat required for phase change
Q = L * m
print(f"Heat required for phase change: Q = {Q}")