python
from scipy.stats import norm
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 100)
y = norm.pdf(x, 0, 1)  # Sannsynlighetstetthetsfunksjon for standard normalfordeling
plt.plot(x, y)
plt.title('Standard normalfordeling')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()