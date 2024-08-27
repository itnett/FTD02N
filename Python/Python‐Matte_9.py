python
import numpy as np
import matplotlib.pyplot as plt

def solve_and_plot_linear_equation(a=1, b=-2):
    """
    Solve and plot a linear equation ax + b = 0.
    
    Parameters:
    a (float): Coefficient of x.
    b (float): Constant term.
    
    Returns:
    x (float): Solution of the equation.
    """
    x = -b / a
    x_values = np.linspace(-10, 10, 400)
    y_values = a * x_values + b

    plt.plot(x_values, y_values, label=f'{a}x + {b} = 0')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.scatter([x], [0], color='red')
    plt.title('Linear Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"GeoGebra input: {a}*x + {b} = 0")
    return x

# Example usage
solve_and_plot_linear_equation()

def solve_and_plot_quadratic_equation(a=1, b=0, c=-4):
    """
    Solve and plot a quadratic equation ax^2 + bx + c = 0.
    
    Parameters:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.
    
    Returns:
    tuple: Solutions of the equation.
    """
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
    else:
        root1 = root2 = None

    x_values = np.linspace(-10, 10, 400)
    y_values = a * x_values**2 + b * x_values + c

    plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c} = 0')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    if root1 is not None and root2 is not None:
        plt.scatter([root1, root2], [0, 0], color='red')
    plt.title('Quadratic Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"GeoGebra input: {a}*x^2 + {b}*x + {c} = 0")
    return root1, root2

# Example usage
solve_and_plot_quadratic_equation()