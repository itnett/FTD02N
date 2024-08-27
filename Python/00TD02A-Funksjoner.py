python
import matplotlib.pyplot as plt
import numpy as np

# 1. Function: f(x) = x + 2
x = np.linspace(-5, 5, 100)
y = x + 2
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="f(x) = x + 2")
plt.title("Linear Function: f(x) = x + 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

# 2. Straight Line: y = 2x + 1
x = np.linspace(-5, 5, 100)
y = 2*x + 1
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="y = 2x + 1")
plt.title("Straight Line: y = 2x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()

# 3. Polynomial Function: f(x) = x^2 and f(x) = x^3
x = np.linspace(-2, 2, 100)
y1 = x**2
y2 = x**3
plt.figure(figsize=(8, 4))
plt.plot(x, y1, label="f(x) = x^2")
plt.plot(x, y2, label="f(x) = x^3")
plt.title("Polynomial Functions")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

# 4. Exponential Function: f(x) = 2^x
x = np.linspace(-2, 4, 100)
y = 2**x
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="f(x) = 2^x")
plt.title("Exponential Function: f(x) = 2^x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

# 5. Derivative of f(x) = x^2 (f'(x) = 2x)
x = np.linspace(-2, 2, 100)
y = x**2
dydx = 2*x
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="f(x) = x^2")
plt.plot(x, dydx, label="f'(x) = 2x")
plt.title("Function and Its Derivative")
plt.xlabel("x")
plt.ylabel("f(x) or f'(x)")
plt.grid(True)
plt.legend()
plt.show()