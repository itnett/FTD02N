python
a, b, c = symbols('a b c')
formula = Eq(a*b, c)
transformed_formula = solve(formula, b)
print("Transformed formula:", transformed_formula)