python
   # Funksjoner: Plotting av eksponentialfunksjon
   import numpy as np
   import matplotlib.pyplot as plt

   x = np.linspace(0, 10, 400)
   y = np.exp(x)

   plt.plot(x, y, label='y = e^x')
   plt.title('Eksponentialfunksjon')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.legend()
   plt.grid(True)
   plt.show()