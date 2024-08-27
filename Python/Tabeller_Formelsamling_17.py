python
import sympy as sp
import numpy as np

# Newtons metode
x = sp.symbols('x')
f = x**2 - 2  # Funksjonen vi vil finne nullpunktet til
x0 = 1.5  # Startverdi

for i in range(5):
    x0 = x0 - f.subs(x, x0) / sp.diff(f, x).subs(x, x0)
print("Tilnærmet nullpunkt:", x0)

# Trapesformelen
def f(x):
    return x**2

a = 0
b = 1
n = 10
h = (b - a) / n
x = np.linspace(a, b, n + 1)
y = f(x)
integral = h * (np.sum(y) - (y[0] + y[-1]) / 2)
print("Tilnærmet integral (trapes):", integral)

# Simpsons formel
integral = h/3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
print("Tilnærmet integral (Simpson):", integral)