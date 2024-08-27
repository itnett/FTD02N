python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def plot_binomial_distribution(n=10, p=0.5):
    """
    Plot the binomial distribution.

    Parameters:
    n (int): Number of trials
    p (float): Probability of success in each trial
    """
    # Generate points for the plot
    x_values = np.arange(0, n+1)
    y_values = stats.binom.pmf(x_values, n, p)
    
    # Plot the binomial distribution
    plt.stem(x_values, y_values, use_line_collection=True)
    plt.title(f'Binomial Distribution (n={n}, p={p})')
    plt.xlabel('Number of successes')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()
    
    print(f"GeoGebra input for binomial distribution: Binomial[{n}, {p}]")

# Example usage with default values
plot_binomial_distribution()