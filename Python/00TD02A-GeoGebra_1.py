python
import numpy as np
import matplotlib.pyplot as plt

# Funksjonen som modellerer væskevolumet
def V(x):
    return 2000 - 2000 * (1 - x / 40) ** 2

# Startvolum
start_volum = V(0)
print("Startvolum:", start_volum, "liter")

# Tidspunktet når volumet når 1000 liter
# Vi bruker numerisk løsning her, siden det ikke er en enkel algebraisk løsning
x_values = np.linspace(0, 40, 1000)  # 1000 punkter mellom 0 og 40 minutter
for i in range(len(x_values) - 1):
    if V(x_values[i]) <= 1000 and V(x_values[i + 1]) >= 1000:
        tid_1000_liter = x_values[i + 1]
        break
print("Volumet når 1000 liter etter:", round(tid_1000_liter, 2), "minutter")

# Maksimalt volum
max_volum = V(40)
print("Maksimalt volum:", max_volum, "liter")

# Grafisk fremstilling
plt.plot(x_values, V(x_values), label="V(x)")
plt.axhline(1000, color='r', linestyle='dashed', linewidth=1, label="1000 liter")
plt.axvline(tid_1000_liter, color='g', linestyle='dashed', linewidth=1, label=f"Tid: {round(tid_1000_liter, 2)} min")
plt.xlabel("Tid (minutter)")
plt.ylabel("Volum (liter)")
plt.title("Modellering av væskevolum over tid")
plt.legend()
plt.grid(True)
plt.show()