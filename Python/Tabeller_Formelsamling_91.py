python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definer en modell
def modell(y, t):
    k = 0.3
    dydt = -k * y
    return dydt

# Initialbetingelse
y0 = 5

# Tidspunkter for løsningen
t = np.linspace(0, 20, 100)

# Løs differensiallikningen
løsning = odeint(modell, y0, t)

# Plot løsningen
plt.plot(t, løsning)
plt.xlabel('Tid')
plt.ylabel('y(t)')
plt.title('Løsning av differensiallikning')
plt.show()