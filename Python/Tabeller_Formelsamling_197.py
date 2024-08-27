python
import matplotlib.pyplot as plt
import numpy as np

# Temperaturer (i Celsius)
T = np.linspace(-10, 110, 100)

# Trykk (i atm) for fasegrensene
p_smelting = np.zeros_like(T) + 1  # Smeltepunktkurve (trykk = 1 atm)
p_fordamping = np.exp(20.386 - 5132 / (T + 273.15))  # Fordampningskurve (Clausius-Clapeyron-ligningen)

# Plott fasediagrammet
plt.plot(T, p_smelting, label='Smelting')
plt.plot(T, p_fordamping, label='Fordamping')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Trykk (atm)')
plt.title('Fasediagram for vann')
plt.legend()
plt.grid(True)
plt.show()