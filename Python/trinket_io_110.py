python
   from sympy import diff

   x = symbols('x')
   poly_function = x ** 3 - 6 * x ** 2 + 11 * x - 6
   poly_derivative = diff(poly_function, x)
   print(f"Den deriverte av polynomfunksjonen: {poly_derivative}")