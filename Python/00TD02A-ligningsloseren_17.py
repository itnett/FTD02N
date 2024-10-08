python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parametre
T = 5
a = -1 / T
tstart = 0
tstop = 25
increment = 1
x0 = 1

# Generere tidspunkter
t = np.arange(tstart, tstop + 1, increment)

# Definerer differensialligningen med parameter
def mydiff(x, t, a):
    return a * x

# Løs differensialligningen
x = odeint(mydiff, x0, t, args=(a,))

# Plotting av resultatet
plt.plot(t, x)
plt.title('Løsning av differensialligning med parameterpassing')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.axis([0, 25, 0, 1])
plt.show()