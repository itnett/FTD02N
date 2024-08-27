python
# Trinket-kode for Leksjon 8.8: Eksponentialregresjon

import numpy as np
import matplotlib.pyplot as plt

# Datasett
x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 8, 16])

# Utfør eksponentialregresjon (log transformasjon av y)
log_y = np.log(y)
coefficients = np.polyfit(x, log_y, 1)
a = np.exp(coefficients[1])
b = np.exp(coefficients[0])

# Print ut koeffisientene
print(f"Leksjon 8.8: Eksponentialregresjon")
print(f"Den beste tilpassede funksjonen er: y = {a:.2f} * {b:.2f}^x")

# Tegn datapunktene og regresjonskurven
x_fit = np.linspace(1, 4, 100)
y_fit = a * b**x_fit
plt.scatter(x, y, color='red', label='Datapunkter')
plt.plot(x_fit, y_fit, label=f'y = {a:.2f} * {b:.2f}^x')
plt.title('Eksponentialregresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()