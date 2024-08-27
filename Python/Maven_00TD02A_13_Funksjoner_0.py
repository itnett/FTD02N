python
import matplotlib.pyplot as plt
import numpy as np

# Rette linje: y = 2x + 3
x = np.linspace(-10, 10, 100)
y = 2 * x + 3

plt.plot(x, y, label='y = 2x + 3')
plt.title("Graf av rett linje")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()