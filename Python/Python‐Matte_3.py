python
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def plot_derivative(a=1, b=0, c=0):
    """
    Plot the function and its derivative.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    """
    # Define the function
    x = sp.symbols('x')
    function = a * x**2 + b * x + c
    
    # Calculate the derivative
    derivative = sp.diff(function, x)
    
    # Convert to numerical functions
    func = sp.lambdify(x, function, modules=['numpy'])
    deriv = sp.lambdify(x, derivative, modules=['numpy'])
    
    # Generate points for the plot
    x_values = np.linspace(-10, 10, 400)
    func_values = func(x_values)
    deriv_values = deriv(x_values)
    
    # Plot the function and its derivative
    plt.plot(x_values, func_values, label=f'{a}x^2 + {b}x + {c}')
    plt.plot(x_values, deriv_values, label=f'Derivative: {derivative}')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Function and its Derivative')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input for function: {a}*x^2 + {b}*x + {c}")
    print(f"GeoGebra input for derivative: {sp.printing.ccode(derivative)}")

# Example usage with default values
plot_derivative()