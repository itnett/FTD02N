python
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_derivative(coeffs=[1, 0, -4]):
    """
    Plot a polynomial function and its derivative.
    
    Parameters:
    coeffs (list): List of coefficients [a_n, a_(n-1), ..., a_1, a_0].
    """
    x = sp.symbols('x')
    polynomial = sum(c * x**i for i, c in enumerate(coeffs))
    derivative = sp.diff(polynomial, x)
    
    p = sp.lambdify(x, polynomial, 'numpy')
    d = sp.lambdify(x, derivative, 'numpy')
    
    x_vals = np.linspace(-10, 10, 400)
    y_vals = p(x_vals)
    dy_vals = d(x_vals)
    
    plt.plot(x_vals, y_vals, label=f'Polynomial: {polynomial}')
    plt.plot(x_vals, dy_vals, label=f'Derivative: {derivative}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Polynomial and its Derivative')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input for polynomial: {polynomial}")
    print(f"GeoGebra input for derivative: {derivative}")

# Example usage
plot_derivative()