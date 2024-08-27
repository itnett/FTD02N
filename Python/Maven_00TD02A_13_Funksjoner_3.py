python
import matplotlib.pyplot as plt
import numpy as np

# Polynomfunksjon: P(x) = x^3 - 3x^2 + 2
x = np.linspace(-1, 3, 400)
y = x**3 - 3*x**2 + 2

# Derivert: P'(x) = 3x^2 - 6x
dy_dx = 3*x**2 - 6*x

plt.plot(x, y, label='P(x) = x^3 - 3x^2 + 2')
plt.plot(x, dy_dx, label="P'(x) = 3x^2 - 6x", linestyle='--')
plt.title("Polynomfunksjon og dens deriverte")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()