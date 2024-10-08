python
# Trinket-kode for Leksjon 8.4: Polynomregresjon

import numpy as np
import matplotlib.pyplot as plt

# Datasett
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

# Utfør polynomregresjon av andre grad
coefficients = np.polyfit(x, y, 2)
polynomial_regression = np.poly1d(coefficients)

# Print ut koeffisientene
print(f"Leksjon 8.4: Polynomregresjon")
print(f"Det beste tilpassede polynomet er: y = {coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]}")

# Tegn datapunktene og regresjonskurven
x_fit = np.linspace(0, 5, 100)
plt.scatter(x, y, color='red', label='Datapunkter')
plt.plot(x_fit, polynomial_regression(x_fit), label=f'y = {coefficients[0]:.2f}x^2 + {coefficients[1]:.2f}x + {coefficients[2]:.2f}')
plt.title('Polynomregresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()