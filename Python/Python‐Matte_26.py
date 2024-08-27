python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def plot_normal_distribution(mean=0, std_dev=1):
    """
    Plot the normal distribution.
    
    Parameters:
    mean (float): Mean of the distribution.
    std_dev (float): Standard deviation of the distribution.
    """
    x_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 400)
    y_values = stats.norm.pdf(x_values, mean, std_dev)
    
    plt.plot(x_values, y_values, label=f'N({mean}, {std_dev}^2)')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(mean, color='red', linestyle='dashed', linewidth=1)
    plt.title('Normal Distribution')
    plt.xlabel('x')
    plt.



[python]

La oss lage Python-kodeeksempler for de matematiske og fysiske temaene som er oppført i emnebeskrivelsen. Hvert eksempel vil være godt kommentert, bruke standardverdier for demonstrasjon, generere grafiske utdata, og inkludere utregninger som kan kopieres til GeoGebra.

### Algebra

#### Regneregler, Brøk og prosentregning, Potenser, Tall på standardform