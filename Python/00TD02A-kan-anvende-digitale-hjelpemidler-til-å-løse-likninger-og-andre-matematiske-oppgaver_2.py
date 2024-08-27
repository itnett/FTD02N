python
import numpy as np

# Define the function
def f(x):
    return x**3 + x - 1

# Initial guess
x0 = 0.5

# Tolerance
tol = 1e-6

# Maximum iterations
max_iter = 100

# Newton-Raphson method
for i in range(max_iter):
    fx = f(x0)
    f_prime_x = 3*x0**2 + 1  # Derivative of f(x)
    x1 = x0 - fx / f_prime_x
    if abs(x1 - x0) < tol:
        break
    x0 = x1

# Print the solution
print("Approximate solution:", x1)