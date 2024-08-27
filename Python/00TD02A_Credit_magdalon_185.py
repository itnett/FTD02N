python
from scipy.optimize import curve_fit
import numpy as np

def modell(x, a, b):
    return a * x + b

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([3, 5, 7, 9, 11])

parametre, _ = curve_fit(modell, x_data, y_data)
a, b = parametre
print(f"Regresjonslinje: y = {a:.2f}x + {b:.2f}")