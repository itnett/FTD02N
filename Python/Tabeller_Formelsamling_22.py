python
import numpy as np

data = np.random.normal(0, 1, 1000)  # Generer 1000 tilfeldige tall fra en normalfordeling
mean = np.mean(data)
std_dev = np.std(data)

k = 2  # Antall standardavvik
within_k_std_dev = np.sum(np.abs(data - mean) <= k * std_dev) / len(data)

print(f"Andel innenfor {k} standardavvik:", within_k_std_dev)
print(f"Tsjebysjevs ulikhet gir en nedre grense på:", 1 - 1/k**2)