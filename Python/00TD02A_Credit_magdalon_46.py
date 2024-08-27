python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Stil 1: Standard
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")
plt.title("Standard stil")
plt.legend()
plt.show()

# Stil 2: Seaborn
with plt.style.context('seaborn'):
    plt.plot(x, y1, label="sin(x)")
    plt.plot(x, y2, label="cos(x)")
    plt.title("Seaborn stil")
    plt.legend()
    plt.show()