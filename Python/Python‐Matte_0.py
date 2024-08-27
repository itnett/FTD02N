python
import matplotlib.pyplot as plt
import numpy as np

def solve_linear_equation(a=1, b=-2):
    """
    Solve the linear equation ax + b = 0 and plot it.

    Parameters:
    a (float): Coefficient of x
    b (float): Constant term

    Returns:
    x (float): Solution of the equation
    """
    # Calculate the solution
    x = -b / a
    
    # Generate points for the plot
    x_values = np.linspace(-10, 10, 400)
    y_values = a * x_values + b
    
    # Plot the line
    plt.plot(x_values, y_values, label=f'{a}x + {b} = 0')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.scatter([x], [0], color='red') # Solution point
    plt.title('Linear Equation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input: {a}*x + {b} = 0")
    
    return x

# Example usage with default values
solve_linear_equation()