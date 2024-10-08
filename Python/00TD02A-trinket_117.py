python
   # Løse likninger av første og andre grad
   from sympy import Eq, solve, symbols

   x = symbols('x')
   linear_eq = Eq(2 * x - 4, 0)
   quadratic_eq = Eq(x**2 - 5 * x + 6, 0)

   linear_solution = solve(linear_eq, x)
   quadratic_solution = solve(quadratic_eq, x)

   print(f"Løsning på lineær likning: {linear_solution}")
   print(f"Løsning på kvadratisk likning: {quadratic_solution}")