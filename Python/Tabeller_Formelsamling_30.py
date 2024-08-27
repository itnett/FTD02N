python
import matplotlib.pyplot as plt
import numpy as np

# Plotting basic geometric shapes
circle = plt.Circle((0.5, 0.5), 0.4, color='blue', fill=False)
square = plt.Rectangle((0.1, 0.1), 0.8, 0.8, color='green', fill=False)
triangle = plt.Polygon(((0.5, 0.9), (0.1, 0.1), (0.9, 0.1)), color='red', fill=False)

fig, ax = plt.subplots()
ax.add_artist(circle)
ax.add_artist(square)
ax.add_artist(triangle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title('Basic Geometric Shapes')
plt.grid(True)
plt.show()