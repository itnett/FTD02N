python
   import matplotlib.pyplot as plt

   x = np.linspace(-10, 10, 400)
   y = 2 * x + 3

   plt.plot(x, y, label='y = 2x + 3')
   plt.title('Rett linje')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.legend()
   plt.grid(True)
   plt.show()