python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 6, 5])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Regression line
regression_line = slope * x + intercept

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, regression_line, color='red', label=f'Linear regression: y = {slope:.2f}x + {intercept:.2f}')
plt.title('Lineær regresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()