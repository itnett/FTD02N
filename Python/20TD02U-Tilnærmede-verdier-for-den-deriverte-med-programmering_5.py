python
# Importere nødvendige biblioteker
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Definere en funksjon
def f(x):
    return x**3 - 3*x**2 + 2*x

# Plot funksjonen og dens deriverte
def plot_function_and_derivative(f):
    x_vals = np.linspace(-1, 3, 400)
    y_vals = f(x_vals)
    
    # Beregne den deriverte symbolsk
    x = sp.symbols('x')
    f_expr = f(x)
    f_prime_expr = sp.diff(f_expr, x)
    f_prime = sp.lambdify(x, f_prime_expr, 'numpy')
    y_prime_vals = f_prime(x_vals)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.plot(x_vals, y_prime_vals, label="f'(x)", linestyle='--')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Funksjon og dens deriverte')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

plot_function_and_derivative(f)