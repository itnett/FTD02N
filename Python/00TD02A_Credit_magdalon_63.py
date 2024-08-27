python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)  # 100 punkter mellom 0 og 2π
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label="sin(x)")
plt.plot(x, y_cos, label="cos(x)")
plt.xlabel("x (radianer)")
plt.ylabel("y")
plt.legend()
plt.title("Sinus- og cosinusfunksjonene")
plt.grid(True)
plt.show()