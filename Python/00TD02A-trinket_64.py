python
   import numpy as np

   # Data
   x_data = np.array([1, 2, 3, 4, 5])
   y_data = np.array([1, 4, 9, 16, 25])

   # Polynomregresjon (grad 2)
   coefficients = np.polyfit(x_data, y_data, 2)
   poly_fit = np.poly1d(coefficients)

   print(f"Polynomregresjon: {poly_fit}")