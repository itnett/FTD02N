python
import numpy as np
import matplotlib.pyplot as plt

# Modellparametre
T = 5
a = -1 / T

# Simuleringsparametre
Ts = 0.01
Tstop = 25
N = int(Tstop / Ts)  # Simuleringslengde
x = np.zeros(N + 1)  # Initialisering av x-vektoren
x[0] = 1  # Initialbetingelse

# Simulering
for k in range(N):
    x[k + 1] = (1 + a * Ts) * x[k]

# Generere tidspunkter
t = np.arange(0, Tstop + Ts, Ts)  # Lage tidsserie

# Plotting av simuleringsresultatet
plt.plot(t, x)
plt.title('Simulering av differensialligning med diskretisering')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.axis([0, 25, 0, 1])
plt.show()