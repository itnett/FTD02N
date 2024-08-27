python
import matplotlib.pyplot as plt


import numpy as np
import scipy.stats as stats

def plot_normal_distribution(mean=0, std_dev=1):
    """
    Plot the normal distribution.

    Parameters:
    mean (float): Mean of the distribution
    std_dev (float): Standard deviation of the distribution
    """
    # Generate points for the plot
    x_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 400)
    y_values = stats.norm.pdf(x_values, mean, std_dev)
    
    # Plot the normal distribution
    plt.plot(x_values, y_values, label=f'N({mean}, {std_dev}^2)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(mean, color='red', linestyle='dashed', linewidth=1) # Mean
    plt.title('Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input for normal distribution: Normal[{mean}, {std_dev}]")

# Example usage with default values
plot_normal_distribution()