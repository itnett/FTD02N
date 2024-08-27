python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Compute and display factorials
factorials = {i: factorial(i) for i in range(1, 16)}
for n, fact in factorials.items():
    print(f"{n}! = {fact}")

# Display Stirling's approximation
import sympy as sp
n = sp.symbols('n')
stirling_approx_lower = n**n * sp.sqrt(2 * sp.pi * n) * sp.exp(-n)
stirling_approx_upper = n**n * sp.sqrt(2 * sp.pi * n) * sp.exp(-n + 1/(12*n))

print(f"Stirling's approximation lower bound: {stirling_approx_lower}")
print(f"Stirling's approximation upper bound: {stirling_approx_upper}")