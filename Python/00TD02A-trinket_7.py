python
   # Tilpasse og omforme formeluttrykk
   from sympy import Eq, solve, symbols

   a, b, c = symbols('a b c')
   formula = Eq(a * b, c)
   transformed_formula = solve(formula, b)
   print(f"Omformet formel: {transformed_formula}")