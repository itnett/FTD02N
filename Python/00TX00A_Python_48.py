python
import matplotlib.pyplot as plt

def plot_data(data):
    """
    Plotter data ved hjelp av matplotlib.

    Parametere:
    data (dict): Ordbok med data som skal plottes

    Returnerer:
    None
    """
    for label, values in data.items():
        plt.plot(values, label=label)
    
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Data Visualization')
    plt.legend()
    plt.grid(True)
    plt.show()

# Eksempel på bruk
data = {"Series 1": [1, 2, 3, 4, 5], "Series 2": [2, 3, 4, 5, 6]}
plot_data(data)