python
   from sympy import symbols, Eq, solve

   # Definere variabler
   x, y = symbols('x y')

   # Definere likninger
   eq1 = Eq(2*x + y, 10)
   eq2 = Eq(x - y, 2)

   # Løse systemet av likninger
   solution = solve((eq1, eq2), (x, y))
   print(f"Løsning: {solution}")