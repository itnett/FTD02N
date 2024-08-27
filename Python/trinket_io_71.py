python
   import matplotlib.pyplot as plt

   # Temperaturdata
   temperatures = [0, 100]
   phases = ["Solid", "Liquid", "Gas"]

   plt.figure()
   plt.plot([0, 100], [0, 100], marker='o')
   plt.xticks(temperatures, phases)
   plt.yticks(temperatures, phases)
   plt.xlabel('Temperature (°C)')
   plt.ylabel('State')
   plt.title('Phase Transitions of Water')
   plt.grid(True)
   plt.show()