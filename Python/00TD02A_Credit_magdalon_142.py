python
import sympy as sy
import matplotlib.pyplot as plt
import numpy as np

# Plotting med Sympy
sy.plot(f, (x, -2, 4))

# Plotting med Matplotlib
f_lambda = lambdify(x, f)
x_verdier = np.linspace(-2, 4, 100)
y_verdier = f_lambda(x_verdier)
plt.plot(x_verdier, y_verdier)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graf av f(x)")
plt.grid(True)
plt.show()