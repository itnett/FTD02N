python
# Trinket-kode for Leksjon 8.6: Potensregresjon

import numpy as np
import matplotlib.pyplot as plt

# Datasett
x = np.array([1, 2, 3, 4])
y = np.array([1, 8, 27, 64])

# Utfør potensregresjon (log-log transformasjon)
log_x = np.log(x)
log_y = np.log(y)
coefficients = np.polyfit(log_x, log_y, 1)
k = np.exp(coefficients[1])
n = coefficients[0]

# Print ut koeffisientene
print(f"Leksjon 8.6: Potensregresjon")
print(f"Den beste tilpassede funksjonen er: y = {k:.2f} * x^{n:.2f}")

# Tegn datapunktene og regresjonskurven
x_fit = np.linspace(1, 4, 100)
y_fit = k * x_fit**n
plt.scatter(x, y, color='red', label='Datapunkter')
plt.plot(x_fit, y_fit, label=f'y = {k:.2f} * x^{n:.2f}')
plt.title('Potensregresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()