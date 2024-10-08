python
   import matplotlib.pyplot as plt
   import numpy as np

   # Definere funksjonen
   def func(x):
       return x**2 + 3*x + 2

   # Generere x-verdier og evaluere funksjonen
   x = np.linspace(-10, 10, 400)
   y = func(x)

   # Plotting
   plt.plot(x, y)
   plt.title('Plot av funksjonen x^2 + 3x + 2')
   plt.xlabel('x')
   plt.ylabel('f(x)')
   plt.grid(True)
   plt.show()