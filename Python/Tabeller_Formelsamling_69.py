python
import sympy as sp

# Definer variabelen
x = sp.symbols('x')

# Løse likning av første grad
eq1 = sp.Eq(3*x + 5, 0)
solution1 = sp.solve(eq1, x)
print(f"Løsning for 3x + 5 = 0: x = {solution1}")

# Løse likning av andre grad
a, b, c = 1, -5, 6
eq2 = sp.Eq(a*x**2 + b*x + c, 0)
solution2 = sp.solve(eq2, x)
print(f"Løsning for x^2 - 5x + 6 = 0: x = {solution2}")

# Løse likningssett med to ukjente
y = sp.symbols('y')
eq1 = sp.Eq(2*x + y, 5)
eq2 = sp.Eq(x - y, 1)
solution_set = sp.solve((eq1, eq2), (x, y))
print(f"Løsning for likningssettet:\n2x + y = 5\nx - y = 1\nLøsning: {solution_set}")

# Tilpasse og omforme formeluttrykk
C, r = sp.symbols('C r')
formula = sp.Eq(C, 2*sp.pi*r)
isolated_r = sp.solve(formula, r)
print(f"Løsning for r i C = 2πr: r = {isolated_r[0]}")

# Eksempel på substitusjonsmetoden
eq3 = sp.Eq(2*x + y, 5)
eq4 = sp.Eq(x - y, 1)
y_solution = sp.solve(eq4, y)[0]
substituted_eq = eq3.subs(y, y_solution)
final_x_solution = sp.solve(substituted_eq, x)[0]
final_y_solution = y_solution.subs(x, final_x_solution)
print(f"Løsning ved substitusjon: x = {final_x_solution}, y = {final_y_solution}")