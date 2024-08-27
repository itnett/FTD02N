python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Initialisering
tstart = 0
tstop = 1
increment = 0.01
x0 = 100

# Generere tidspunkter
t = np.arange(tstart, tstop + increment, increment)

# Funksjon som returnerer dx/dt
def bacteriadiff(x, t):
    b = 1
    p = 0.5
    return b * x - p * x**2

# Løs differensialligningen
x = odeint(bacteriadiff, x0, t)

# Plotting av resultatet
plt.plot(t, x)
plt.title('Bakteriesimulering')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.axis([0, 1, 0, 100])
plt.show()