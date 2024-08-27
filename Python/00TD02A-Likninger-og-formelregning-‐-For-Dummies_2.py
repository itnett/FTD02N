python
# Trinket-kode for Leksjon 3: Tilpasse og Omforme Formeluttrykk

from sympy import symbols, Eq, solve

# Eksempel 1: Isolere x i formelen y = 3x + 2
x, y = symbols('x y')
formel = Eq(y, 3*x + 2)
isolert_x = solve(formel, x)
print(f"Isolere x i formelen y = 3x + 2: x = {isolert_x[0]}")

# Eksempel 2: Tilpasse formelen V = lwh for å isolere h
V, l, w, h = symbols('V l w h')
formel2 = Eq(V, l*w*h)
isolert_h = solve(formel2, h)
print(f"Isolere h i formelen V = lwh: h = {isolert_h[0]}")

# Visualisering av omformet formel
import matplotlib.pyplot as plt
import numpy as np

# Visualisering av formelen y = 3x + 2 og isolert formel
x_vals = np.linspace(-10, 10, 400)
y_vals = 3*x_vals + 2
x_isolert_vals = (y_vals - 2) / 3

plt.plot(x_vals, y_vals, label='y = 3x + 2')
plt.plot(x_isolert_vals, y_vals, label='x isolert: x = (y - 2) / 3', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Tilpasse og Omforme Formeluttrykk')
plt.legend()
plt.grid(True)
plt.show()