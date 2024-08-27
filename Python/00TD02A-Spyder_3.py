python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = x**2  # Eksempel på en funksjon

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graf av funksjonen y = x^2')
plt.show()