python
import matplotlib.pyplot as plt
import numpy as np

def solve_quadratic_equation(a=1, b=0, c=-4):
    """
    Solve the quadratic equation ax^2 + b^2 + c = 0 and plot it.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    roots (tuple): Solutions of the equation
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the two solutions
    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
    else:
        root1 = root2 = None
    
    # Generate points for the plot
    x_values = np.linspace(-10, 10, 400)
    y_values = a * x_values**2 + b * x_values + c
    
    # Plot the quadratic function
    plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    if root1 is not None and root2 is not None:
        plt.scatter([root1, root2], [0, 0], color='red') # Solution points
    plt.title('Quadratic Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input: {a}*x^2 + {b}*x + {c} = 0")
    
    return root1, root2

# Example usage with default values
solve_quadratic_equation()