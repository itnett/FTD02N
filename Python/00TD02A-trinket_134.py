python
   # Sammentrekning og faktorisering
   from sympy import symbols, expand, factor

   x, y = symbols('x y')
   expr = x**2 - y**2
   expanded_expr = expand(expr)
   factored_expr = factor(expanded_expr)
   print(f"Ekspandert uttrykk: {expanded_expr}")
   print(f"Faktorisert uttrykk: {factored_expr}")