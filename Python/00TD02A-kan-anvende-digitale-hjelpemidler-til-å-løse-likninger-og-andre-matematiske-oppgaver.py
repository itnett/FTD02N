python
import matplotlib.pyplot as plt
import numpy as np

# Simulated network traffic data (time in seconds, packets per second)
time = np.arange(0, 60, 1)
packets = 100 + 50 * np.sin(0.1 * time) + np.random.normal(0, 10, 60)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(time, packets)
plt.title('Network Traffic Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Packets per Second')
plt.grid(True)
plt.show()