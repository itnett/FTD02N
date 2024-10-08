python
import matplotlib.pyplot as plt
import numpy as np

# Konstanter
g = 9.81  # Tyngdeakselerasjonen i m/s^2
l = 1.0   # Lengden av pendelen i meter
theta_0 = 0.2  # Maksimalt vinkelutslag i radianer

# Tidsvariabler
t = np.linspace(0, 10, 1000)  # 10 sekunder, 1000 punkter

# Pendelens bevegelsesligning for små svingninger
theta = theta_0 * np.cos(np.sqrt(g/l) * t)

# Plotting
plt.plot(t, theta)
plt.xlabel('Tid (s)')
plt.ylabel('Vinkelutslag (rad)')
plt.title('Pendelens Svingninger')
plt.grid(True)
plt.show()