python
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Demonstrating angle conversion and plotting sine and cosine functions
angle_degrees = 45
angle_radians = np.deg2rad(angle_degrees)

print(f"{angle_degrees} degrees in radians is {angle_radians}")

# Plotting sine and cosine functions
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.xlabel('x (radians)')
plt.ylabel('Function value')
plt.legend()
plt.title('Sine and Cosine functions')
plt.grid(True)
plt.show()