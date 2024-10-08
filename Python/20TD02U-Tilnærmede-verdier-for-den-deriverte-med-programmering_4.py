python
# Importere nødvendige biblioteker
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definere funksjonen f(x)
def f(x):
    return x**3 - 2*x**2 + x - 3

# Finne røttene til funksjonen f(x)
def find_roots(f):
    x = sp.symbols('x')
    roots = sp.solve(f(x), x)
    return roots

# Plot funksjonen og markere røttene
def plot_function_and_roots(f):
    x_vals = np.linspace(-3, 3, 400)
    y_vals = f(x_vals)
    roots = find_roots(f)
    
    plt.plot(x_vals, y_vals, label='f(x)')
    for root in roots:
        plt.plot(root, f(root), 'ro')
        plt.text(root, f(root), f'  x = {root:.2f}', ha='left')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Graf av funksjonen f(x) og dens røtter')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

# Kjøre plot funksjonen
plot_function_and_roots(f)