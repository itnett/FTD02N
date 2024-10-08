python
from sympy import Eq, solve
x = symbols('x')
linear_eq = Eq(2*x - 4, 0)
quadratic_eq = Eq(x**2 - 5*x + 6, 0)
linear_solution = solve(linear_eq, x)
quadratic_solution = solve(quadratic_eq, x)
print("Linear equation solution:", linear_solution)
print("Quadratic equation solutions:", quadratic_solution)