python
   import numpy as np

   # Definere polynomfunksjon
   def poly_function(x):
       return x**3 - 6*x**2 + 11*x - 6

   # Evaluere funksjonen over et intervall
   x_values = np.linspace(-10, 10, 400)
   y_values = poly_function(x_values)

   print(f"Evaluert polynomfunksjon: {y_values}")