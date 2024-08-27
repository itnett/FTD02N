python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=50, scale=10, size=1000)  # Generer 1000 tilfeldige tall fra en normalfordeling

plt.hist(data, bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram av tilfeldige tall")
plt.xlabel("Verdi")
plt.ylabel("Frekvens")
plt.show()