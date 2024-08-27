python
import matplotlib.pyplot as plt
import numpy as np

# Polynomfunksjon: P(x) = x^3 - 6x^2 + 11x - 6
x = np.linspace(-1, 4, 400)
y = x**3 - 6*x**2 + 11*x - 6

plt.plot(x, y, label='P(x) = x^3 - 6x^2 + 11x - 6')
plt.title("Graf av polynomfunksjon")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()