python
import matplotlib.pyplot as plt
import numpy as np

# Network capacity parameters
bandwidth = 100  # Mbps
num_users = np.arange(1, 101)  # 1 to 100 users
data_per_user = 5  # Mbps

# Calculate available bandwidth per user
bandwidth_per_user = bandwidth / num_users

# Plot
plt.figure(figsize=(10, 6))
plt.plot(num_users, bandwidth_per_user, marker='o', linestyle='-')
plt.title('Network Capacity vs. Number of Users')
plt.xlabel('Number of Users')
plt.ylabel('Available Bandwidth per User (Mbps)')
plt.grid(True)
plt.show()