python
import numpy as np
import matplotlib.pyplot as plt

def cpu_bruk(t):
    return 0.2 * np.sin(2 * np.pi * t / 24) + 0.8  # Simulert CPU-bruk over 24 timer

t = np.linspace(0, 24, 100)
plt.plot(t, cpu_bruk(t))
plt.xlabel("Tid (timer)")
plt.ylabel("CPU-bruk")
plt.title("Simulert CPU-bruk over 24 timer")
plt.grid(True)
plt.show()