python
import matplotlib.pyplot as plt

# Definere masse og kraft
mass = 10  # kg
force = [10, 20, 30, 40, 50]  # Newton

# Beregne akselerasjon
acceleration = [f/mass for f in force]

plt.plot(force, acceleration, marker='o')
plt.title("Newtons andre lov: Akselerasjon som funksjon av Kraft")
plt.xlabel("Kraft (N)")
plt.ylabel("Akselerasjon (m/s²)")
plt.grid(True)
plt.show()