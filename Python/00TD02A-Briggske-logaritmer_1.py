python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 10, 100, 1000, 10000])
y = np.log10(x)

plt.plot(x, y, marker='o')
plt.xscale('log')
plt.xlabel('Number')
plt.ylabel('Logarithm (Base 10)')
plt.title('Logarithm Base 10 Graph')
plt.grid(True)
plt.show()