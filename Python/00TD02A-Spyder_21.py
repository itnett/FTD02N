python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Uavhengig variabel
y = np.array([1, 4, 9, 16, 25])  # Avhengig variabel

poly = PolynomialFeatures(degree=2)  # Polynom av grad 2
x_poly = poly.fit_transform(x)

modell = LinearRegression()
modell.fit(x_poly, y)

# Visualisering
plt.scatter(x, y, color='blue')
plt.plot(x, modell.predict(x_poly), color='red')
plt.title('Polynomregresjon (grad 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()