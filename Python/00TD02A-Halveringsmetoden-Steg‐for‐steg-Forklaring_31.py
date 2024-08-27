python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + x - 1

# Initial interval
a, b = 0, 1

# Tolerance (desired accuracy)
tolerance = 0.0001

# List to store the midpoints for visualization
midpoints = []

# Bisection method loop
while (b - a) / 2 > tolerance:
    midpoint = (a + b) / 2
    midpoints.append(midpoint)

    if f(midpoint) == 0:
        break
    elif f(a) * f(midpoint) < 0:
        b = midpoint
    else:
        a = midpoint

# Approximate root
root = (a + b) / 2

# Visualization
x = np.linspace(0, 1, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x^3 + x - 1')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.plot(root, f(root), 'ro', label=f'Root ≈ {root:.3f}')  # Mark the root

# Visualize the bisection steps
for i, m in enumerate(midpoints):
    plt.plot([a, b], [f(a), f(b)], 'g:')  # Interval line
    plt.plot([m, m], [0, f(m)], 'b:')     # Vertical line at midpoint
    plt.text(m, f(m) + 0.1, f'm{i+1}', ha='center')  # Label midpoints

plt.title('Bisection Method')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()