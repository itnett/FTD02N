python
from sympy import diff

# Deriver funksjonen f(x)
df = diff(f, x)
print(df)  # Output: Piecewise((-1, x < 0), (1, True))