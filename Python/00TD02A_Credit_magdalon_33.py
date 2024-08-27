python
import matplotlib.pyplot as plt

tidspunkter = ["09:00", "10:00", "11:00", "12:00", "13:00"]
trafikk_kbps = [100, 150, 200, 250, 300]

plt.plot(tidspunkter, trafikk_kbps, marker='o', linestyle='-', color='blue')
plt.title("Nettverkstrafikk over tid")
plt.xlabel("Tidspunkt")
plt.ylabel("Trafikk (kbps)")
plt.grid(axis='y', linestyle='--')
plt.show()