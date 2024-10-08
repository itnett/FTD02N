python
import matplotlib.pyplot as plt

responstider = [45, 52, 68, 39, 58, 48, 72, 63, 55, 61]  # Responstider i millisekunder

plt.hist(responstider, bins=[0, 20, 40, 60, 80, 100], edgecolor="black")
plt.title("Histogram av responstider")
plt.xlabel("Responstid (ms)")
plt.ylabel("Antall forespørsler")
plt.show()