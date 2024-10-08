python
import matplotlib.pyplot as plt

# Error data
total_requests = 10000
error_count = 250

# Calculate error rate
error_rate = (error_count / total_requests) * 100

# Plot
plt.figure(figsize=(8, 4))
plt.bar(["Error Rate"], [error_rate], color='red')
plt.title('Error Rate')
plt.ylabel('Percentage (%)')
plt.ylim(0, 10)  # Set y-axis limits for better visualization
plt.show()