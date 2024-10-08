python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)  # Tid (0 til 10 sekunder)
a = 9.81  # Tyngdeakselerasjon (m/s^2)

# Fritt fall
y = 0.5 * a * t**2
plt.plot(t, y, label='Fritt fall')

# Bevegelse med konstant fart
v0 = 5  # Startfart (m/s)
y_konstant_fart = v0 * t
plt.plot(t, y_konstant_fart, label='Konstant fart')

plt.xlabel('Tid (s)')
plt.ylabel('Høyde (m)')
plt.title('Bevegelse med konstant akselerasjon og konstant fart')
plt.legend()
plt.show()