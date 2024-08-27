python
import numpy as np
import matplotlib.pyplot as plt

# Planvinkel
def planvinkel(b, R):
    return b / R

# Example for planvinkel
b = 5  # Arc length
R = 10  # Radius
v = planvinkel(b, R)
print(f"Planvinkel (radians) = {v}")

# Conversion between degrees, grads, and radians
degree_to_radian = np.pi / 180
grad_to_radian = np.pi / 200

print(f"1 degree in radians = {degree_to_radian}")
print(f"1 grad in radians = {grad_to_radian}")

# Romvinkel
def romvinkel(A, R):
    return A / R**2

# Example for romvinkel
A = 20  # Area
R = 5  # Radius
Omega = romvinkel(A, R)
print(f"Romvinkel (steradians) = {Omega}")

# Plotting example
theta = np.linspace(0, 2 * np.pi, 100)
r = np.ones_like(theta) * R
x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure()
plt.plot(x, y, label='Circle of radius R')
plt.title('Circle and Planvinkel')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()