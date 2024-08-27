python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Function")
plt.show()