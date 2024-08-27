python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-5, 5, 100)  # 100 punkter mellom -5 og 5
y = f(x)

plt.plot(x, y, label="f(x) = x^2")
plt.title("Graf av en kvadratisk funksjon")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()