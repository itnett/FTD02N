python
import sympy as sp

# Define the constants
pi = sp.pi
e = sp.E
gamma = sp.EulerGamma

# Display the constants
print(f"pi = {pi.evalf()}")
print(f"e = {e.evalf()}")
print(f"gamma = {gamma.evalf()}")

# Define limits
n = sp.symbols('n')
e_limit = sp.limit((1 + 1/n)**n, n, sp.oo)
gamma_limit = sp.limit(sp.Sum(1/k for k in range(1, n+1)) - sp.log(n), n, sp.oo)

# Display the limits
print(f"e (limit) = {e_limit}")
print(f"gamma (Euler's constant) = {gamma_limit}")