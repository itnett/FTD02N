python
import sympy as sp

# Define symbols
x = sp.symbols('x')

# Equation to solve
equation = sp.Eq(x**2 + 3*x - 4, 0)

# Solve the equation
solutions = sp.solve(equation)

# Print the solutions
print("Solutions:", solutions)