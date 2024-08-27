python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Eksempeldata
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

# Tilpasse lineær regresjon
modell = LinearRegression()
modell.fit(x.reshape(-1, 1), y)  # x må være en 2D-array

# Hente ut stigningstall og konstantledd
a = modell.coef_[0]
b = modell.intercept_

# Predikere verdier
x_pred = np.array([6, 7])
y_pred = modell.predict(x_pred.reshape(-1, 1))

# Visualisere resultatene
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, a*x + b, color='red', label='Regresjonslinje')
plt.scatter(x_pred, y_pred, color='green', label='Prediksjoner')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()