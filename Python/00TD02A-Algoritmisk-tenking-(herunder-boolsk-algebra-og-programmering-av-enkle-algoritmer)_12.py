python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.legend()
plt.title('Sin and Cos Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()