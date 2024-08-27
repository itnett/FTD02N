python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initialisering
tstart = -1
tstop = 1
increment = 0.1
x0 = [1, 1]

# Generere tidspunkter
t = np.arange(tstart, tstop + increment, increment)

# Funksjon som returnerer dx/dt for systemet
def mydiff(x, t):
    dx1dt = -x[1]
    dx2dt = x[0]
    return [dx1dt, dx2dt]

# Løs differensialligningen
x = odeint(mydiff, x0, t)

# Hente ut løsninger
x1 = x[:, 0]
x2 = x[:, 1]

# Plotting av resultatene
plt.plot(t, x1, label='x1')
plt.plot(t, x2, label='x2')
plt.title('Simulering med to variabler')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.axis([-1, 1, -1.5, 1.5])
plt.legend()
plt.show()