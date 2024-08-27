python
from sympy import solveset, diff

# Finn nullpunktene til f(x)
nullpunkter = solveset(f, x)
print(nullpunkter)  # Output: {-1, 1, 3}

# Deriver f(x)
df = diff(f, x)
print(df)  # Output: x**2 - 2*x - 1/3

# Finn ekstremalpunktene til f(x)
ekstremalpunkter = solveset(df, x)
print(ekstremalpunkter)