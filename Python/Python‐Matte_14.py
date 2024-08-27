python
import numpy as np
import matplotlib.pyplot as plt

def plot_linear_function(m=1, c=0):
    """
    Plot a linear function y = mx + c.
    
    Parameters:
    m (float): Slope of the line.
    c (float): y-intercept.
    """
    x = np.linspace(-10, 10, 400)
    y = m * x + c
    plt.plot(x, y, label=f'y = {m}x + {c}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Linear Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input: y = {m}x + {c}")

def plot_polynomial_function(coeffs=[1, 0, -4]):
    """
    Plot a polynomial function.
    
    Parameters:
    coeffs (list): List of coefficients [a_n, a_(n-1), ..., a_1, a_0].
    """
    p = np.poly1d(coeffs)
    x = np.linspace(-10, 10, 400)
    y = p(x)
    plt.plot(x, y, label=f'y = {" ".join([f"{a}x^{i}" for i, a in enumerate(coeffs[::-1])])}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Polynomial Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input: Polynomial[{', '.join(map(str, coeffs))}]")

def plot_exponential_function(base=2):
    """
    Plot an exponential function y = base^x.
    
    Parameters:
    base (float): Base of the exponential function.
    """
    x = np.linspace(-2, 2, 400)
    y = base ** x
    plt.plot(x, y, label=f'y = {base}^x')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Exponential Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input: y = {base}^x")

# Example usage
plot_linear_function()
plot_polynomial_function()
plot_exponential_function()