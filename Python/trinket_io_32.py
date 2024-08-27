python
import numpy as np

x = np.linspace(-10, 10, 400)
poly_function = x**3 - 6*x**2 + 11*x - 6
print(f"Polynomial function evaluated over range: {poly_function}")