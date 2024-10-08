python
import matplotlib.pyplot as plt
import numpy as np

# Parameters
distance = np.arange(1, 101)  # Distance in meters
initial_power = 10  # Initial signal power in mW
attenuation = 0.2  # Attenuation per meter in dB

# Calculate signal power at each distance
signal_power = initial_power * 10**(-attenuation * distance / 10)

# Plot
plt.plot(distance, signal_power)
plt.title('Signal Power vs. Distance')
plt.xlabel('Distance (m)')
plt.ylabel('Signal Power (mW)')
plt.yscale('log')  # Logarithmic scale for y-axis
plt.grid(True)
plt.show()