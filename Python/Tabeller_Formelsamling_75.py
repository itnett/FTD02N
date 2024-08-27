python
import sympy as sp

# Define a symbol
x = sp.symbols('x')

# Base 10 logarithm (Briggsian logarithm)
log10 = sp.log(x, 10)
print(f"Base 10 logarithm of x: {log10}")