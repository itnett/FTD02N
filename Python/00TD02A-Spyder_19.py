python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Pendelparametere
L = 1.0  # Lengde (m)
g = 9.81  # Tyngdeakselerasjon (m/s^2)
theta0 = np.radians(30)  # Startvinkel (radianer)
omega0 = 0  # Starthastighet (rad/s)

def pendel(y, t):
    theta, omega = y
    dydt = [omega, -g/L * np.sin(theta)]
    return dydt

t = np.linspace(0, 10, 100)
y0 = [theta0, omega0]
sol = odeint(pendel, y0, t)

theta = sol[:, 0]

# Visualisering
plt.plot(t, np.degrees(theta))
plt.xlabel('Tid (s)')
plt.ylabel('Vinkel (grader)')
plt.title('Pendelbevegelse')
plt.grid(True)
plt.show()