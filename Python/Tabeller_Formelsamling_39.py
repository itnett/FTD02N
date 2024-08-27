python
import matplotlib.pyplot as plt
import numpy as np

# Plotting a circle with a central and peripheral angle
fig, ax = plt.subplots()

# Circle parameters
R = 5
theta = np.linspace(0, 2 * np.pi, 100)
x = R * np.cos(theta)
y = R * np.sin(theta)

# Plot circle
ax.plot(x, y, label='Circle')

# Points on the circle
A = (R * np.cos(np.pi/4), R * np.sin(np.pi/4))
B = (R * np.cos(-np.pi/4), R * np.sin(-np.pi/4))
O = (0, 0)

# Plot points
ax.plot(*A, 'ro')
ax.plot(*B, 'ro')
ax.plot(*O, 'bo')

# Plot lines
ax.plot([A[0], O[0]], [A[1], O[1]], 'g--', label='Radius')
ax.plot([B[0], O[0]], [B[1], O[1]], 'g--')
ax.plot([A[0], B[0]], [A[1], B[1]], 'b--', label='Chord')

# Adding labels
ax.text(A[0], A[1], 'A', fontsize=12, ha='right')
ax.text(B[0], B[1], 'B', fontsize=12, ha='right')
ax.text(O[0], O[1], 'O', fontsize=12, ha='right')

ax.set_aspect('equal', 'box')
ax.grid(True)
ax.legend()
plt.title('Periphery Angle Theorem')
plt.xlabel('x')
plt.ylabel('y')
plt.show()