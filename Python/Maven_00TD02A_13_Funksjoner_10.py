python
import numpy as np
import matplotlib.pyplot as plt

# Rette linjer: y = 2x + 3
x = np.linspace(-10, 10, 100)
y = 2 * x + 3
plt.plot(x, y, label='y = 2x + 3')

# Polynomfunksjon: P(x) = x^3 - 6x^2 + 11x - 6
y_poly = x**3 - 6*x**2 + 11*x - 6
plt.plot(x, y_poly, label='P(x) = x^3 - 6x^2 + 11x - 6')

# Eksponentialfunksjon: f(x) = 2 * 3^x
y_exp = 2 * 3**x
plt.plot(x, y_exp, label='f(x) = 2 * 3^x')

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title("Funksjoner")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()