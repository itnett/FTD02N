python
import matplotlib.pyplot as plt
import numpy as np

def plot_trigonometric_functions():
    """
    Plot the sine and cosine functions.
    """
    # Generate points for the plot
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    sin_values = np.sin(x_values)
    cos_values = np.cos(x_values)
    
    # Plot the sine function
    plt.plot(x_values, sin_values, label='sin(x)')
    plt.plot(x_values, cos_values, label='cos(x)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Trigonometric Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("GeoGebra input for sine: sin(x)")
    print("GeoGebra input for cosine: cos(x)")

# Example usage
plot_trigonometric_functions()