python
y = symbols('y')
eq1 = Eq(2*x + y, 10)
eq2 = Eq(x - y, 2)
system_solution = solve((eq1, eq2), (x, y))
print("System of equations solution:", system_solution)