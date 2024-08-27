python
import matplotlib.pyplot as plt
import numpy as np

# Eksponentialfunksjon: f(x) = 2 * 3^x
x = np.linspace(-2, 2, 400)
y = 2 * 3**x

plt.plot(x, y, label='f(x) = 2 * 3^x')
plt.title("Graf av eksponentialfunksjon")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()