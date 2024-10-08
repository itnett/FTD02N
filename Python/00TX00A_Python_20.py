python
import matplotlib.pyplot as plt

def rette_linjer(a=1, b=2, x_range=(0, 10)):
    """
    Plotter en rett linje gitt ved y = ax + b.
    
    Parametere:
    a (int/float): Stigningstallet (standardverdi 1)
    b (int/float): Konstantleddet (standardverdi 2)
    x_range (tuple): Område for x-verdiene (standardverdi (0, 10))
    
    Returnerer:
    None
    """
    x = list(range(x_range[0], x_range[1] + 1))
    y = [a * xi + b for xi in x]
    
    plt.plot(x, y, label=f'y = {a}x + {b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Rett linje')
    plt.legend()
    plt.grid(True)
    plt.show()

# Eksempel på bruk
rette_linjer()