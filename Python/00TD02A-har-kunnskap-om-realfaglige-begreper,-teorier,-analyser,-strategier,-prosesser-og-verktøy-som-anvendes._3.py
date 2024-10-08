python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
power = 100  # Watts
time = np.arange(0, 60, 1)  # Time in seconds
heat_capacity = 1000  # Joules per degree Celsius
initial_temperature = 20  # °C

# Calculate temperature rise
temperature = initial_temperature + (power * time) / heat_capacity

# Plot
plt.plot(time, temperature)
plt.title('Temperature Rise Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()