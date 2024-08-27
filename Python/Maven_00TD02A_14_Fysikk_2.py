python
import matplotlib.pyplot as plt

# Målinger med forskjellige nivåer av usikkerhet
measurements = [5.34, 5.3, 5.0]  # Eksempel på målinger i cm
errors = [0.02, 0.05, 0.1]  # Usikkerhet i målingene

plt.errorbar([1, 2, 3], measurements, yerr=errors, fmt='o', capsize=5, color='red')
plt.title("Målinger med Usikkerhet")
plt.xlabel("Måling Nummer")
plt.ylabel("Lengde (cm)")
plt.show()