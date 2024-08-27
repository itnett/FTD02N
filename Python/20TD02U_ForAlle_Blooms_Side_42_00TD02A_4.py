python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Gitt et datasett av punkter
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# Utfør lineær regresjon
model = LinearRegression().fit(X, y)
y_pred = model.predict(X)

# Visualiser resultatet
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.show()