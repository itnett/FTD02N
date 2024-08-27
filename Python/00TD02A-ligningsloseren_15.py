python
import numpy as np
import matplotlib.pyplot as plt

# Parametre
T = 5
a = -1 / T
x0 = 1
tstart = 0
tstop = 25
increment = 1

# Generere tidspunkter
t = np.arange(tstart, tstop + 1, increment)

# Løsning av differensialligningen analytisk
x = x0 * np.exp(a * t)

# Plotting av resultatet
plt.plot(t, x)
plt.title('Løsning av differensialligning analytisk')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.axis([0, 25, 0, 1])
plt.show()