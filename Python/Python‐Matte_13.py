python
import numpy as np
import matplotlib.pyplot as plt

def plot

_vectors(v1=(1, 2), v2=(3, 4)):
    """
    Plot two vectors in the plane.
    
    Parameters:
    v1, v2 (tuple): Coordinates of the vectors.
    """
    origin = np.array([0, 0])
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    plt.quiver(*origin, *v1, color='r', scale=1, scale_units='xy', angles='xy', label='v1')
    plt.quiver(*origin, *v2, color='b', scale=1, scale_units='xy', angles='xy', label='v2')
    plt.xlim(-1, 5)
    plt.ylim(-1, 5)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()
    
    print(f"GeoGebra input for v1: Vector[(0, 0), ({v1[0]}, {v1[1]})]")
    print(f"GeoGebra input for v2: Vector[(0, 0), ({v2[0]}, {v2[1]})]")

# Example usage
plot_vectors()