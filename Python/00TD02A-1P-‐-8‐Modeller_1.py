python
# Trinket-kode for Leksjon 8.2: Lineær regresjon

import numpy as np
import matplotlib.pyplot as plt

# Datasett
x = np.array([1, 2, 3, 4])
y = np.array([2, 3, 5, 4])

# Utfør lineær regresjon
coefficients = np.polyfit(x, y, 1)
linear_regression = np.poly1d(coefficients)

# Print ut koeffisientene
print(f"Leksjon 8.2: Lineær regresjon")
print(f"Den beste tilpassede linjen er: y = {coefficients[0]}x + {coefficients[1]}")

# Tegn datapunktene og regresjonslinjen
plt.scatter(x, y, color='red', label='Datapunkter')
plt.plot(x, linear_regression(x), label=f'y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}')
plt.title('Lineær regresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()