python
import matplotlib.pyplot as plt
import numpy as np

# Definere masser
masses = np.array([1, 5, 10, 20])  # i kg
gravity = 9.81  # m/s^2 (jordens gravitasjonsfelt)

# Beregne tyngde
weights = masses * gravity  # i Newton

plt.bar(masses, weights, color='green')
plt.title("Forholdet mellom Masse og Tyngde på Jorden")
plt.xlabel("Masse (kg)")
plt.ylabel("Tyngde (N)")
plt.show()