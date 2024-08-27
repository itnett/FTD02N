python
import matplotlib.pyplot as plt
import numpy as np

# Ellipse
t = np.linspace(0, 2 * np.pi, 100)
a = 2
b = 1
plt.plot(a * np.cos(t), b * np.sin(t))
plt.title('Ellipse')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# Hyperbel
t = np.linspace(-2, 2, 100)
a = 1
b = 1
plt.plot(a * np.cosh(t), b * np.sinh(t))
plt.plot(-a * np.cosh(t), b * np.sinh(t))  # Den andre grenen av hyperbelen
plt.title('Hyperbel')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# Parabel
x = np.linspace(-5, 5, 100)
a = 1
y = a * x**2
plt.plot(x, y)
plt.title('Parabel')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()