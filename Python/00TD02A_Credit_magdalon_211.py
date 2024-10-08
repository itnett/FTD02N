python
   import matplotlib.pyplot as plt

   time_points = ["09:00", "10:00", "11:00", "12:00", "13:00"]
   traffic_kbps = [100, 150, 200, 250, 300]

   plt.plot(time_points, traffic_kbps, marker='o', linestyle='-', color='blue')
   plt.title("Network Traffic Over Time")
   plt.xlabel("Time")
   plt.ylabel("Traffic (kbps)")
   plt.grid(axis='y', linestyle='--')
   plt.show()