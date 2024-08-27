python
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def plot_integral(a=1, b=0, c=0, lower_limit=0, upper_limit=1):
    """
    Plot the function and its definite integral over a given interval.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    lower_limit (float): Lower limit of integration
    upper_limit (float): Upper limit of integration
    """
    # Define the function
    x = sp.symbols('x')
    function = a * x**2 + b * x + c
    
    # Calculate the definite integral
    integral = sp.integrate(function, (x, lower_limit, upper_limit))
    
    # Convert to numerical function
    func = sp.lambdify(x, function, modules=['numpy'])
    
    # Generate points for the plot
    x_values = np.linspace(-10, 10, 400)
    func_values = func(x_values)
    
    # Plot the function
    plt.plot(x_values, func_values, label=f'{a}x^2 + {b}x + {c}')
    plt.fill_between(x_values, func_values, where=(x_values >= lower_limit) & (x_values <= upper_limit), color='grey', alpha=0.5)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title(f'Function and its Definite Integral from {lower_limit} to {upper_limit}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input for function: {a}*x^2 + {b}*x + {c}")
    print(f"GeoGebra input for integral: Integrate[{a}*x^2 + {b}*x + {c}, {lower_limit}, {upper_limit}] = {integral}")

# Example usage with default values
plot_integral()