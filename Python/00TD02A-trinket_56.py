python
   from sympy import symbols, diff

   # Definere variabel og funksjon
   x = symbols('x')
   func = x**2 + 3*x + 2

   # Beregne den deriverte av funksjonen
   derivative = diff(func, x)
   print(f"Funksjon: {func}")
   print(f"Derivert: {derivative}")