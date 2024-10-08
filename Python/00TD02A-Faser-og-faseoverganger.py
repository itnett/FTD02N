python
import matplotlib.pyplot as plt

# Define events and times
events = ["Attack starts", "Firewall breached", "Data exfiltrated", "Intrusion detected", "Incident response initiated", "Attack contained"]
times = [0, 5, 10, 15, 20, 30]

# Create the timeline plot
plt.figure(figsize=(12, 2))
plt.hlines(0, 0, max(times) + 5, colors="gray", linestyles="dashed")
plt.eventplot(times, orientation='horizontal', colors='red', linelengths=0.8)
plt.yticks([0], [""])  # Remove y-axis ticks and labels
plt.xlabel("Time")
plt.title("Cyberattack Timeline")

# Add event labels
for time, event in zip(times, events):
    plt.text(time, 0.1, event, ha='center', va='bottom')

plt.show()