python
# Trinket-kode for Leksjon 1: Løse Likninger av Første og Andre Grad

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Likning av første grad: 2x + 3 = 7
x = symbols('x')
likning1 = Eq(2*x + 3, 7)
losning1 = solve(likning1, x)

print(f"Løsningen for likningen 2x + 3 = 7 er: x = {losning1[0]}")

# Visualisering av likning av første grad
x_vals = np.linspace(-10, 10, 400)
y_vals = 2*x_vals + 3
plt.plot(x_vals, y_vals, label='y = 2x + 3')
plt.axhline(7, color='red', linestyle='--', label='y = 7')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Likning av Første Grad: 2x + 3 = 7')
plt.legend()
plt.grid(True)
plt.show()

# Likning av andre grad: x^2 - 5x + 6 = 0
likning2 = Eq(x**2 - 5*x + 6, 0)
losninger2 = solve(likning2, x)

print(f"Løsningene for likningen x^2 - 5x + 6 = 0 er: x = {losninger2[0]} og x = {losninger2[1]}")

# Visualisering av likning av andre grad
y_vals = x_vals**2 - 5*x_vals + 6
plt.plot(x_vals, y_vals, label='y = x^2 - 5x + 6')
plt.axhline(0, color='red', linestyle='--', label='y = 0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Likning av Andre Grad: x^2 - 5x + 6 = 0')
plt.legend()
plt.grid(True)
plt.show()