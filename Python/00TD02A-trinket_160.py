python
   # Funksjoner: Plotting av polynomfunksjon
   import numpy as np
   import matplotlib.pyplot as plt

   x = np.linspace(-10, 10, 400)
   y = x ** 3 - 6 * x ** 2 + 11 * x - 6

   plt.plot(x, y, label='y = x^3 - 6x^2 + 11x - 6')
   plt.title('Polynomfunksjon')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.legend()
   plt.grid(True)
   plt.show()