python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Uavhengig variabel
y = np.array([2, 4, 5, 4, 5])  # Avhengig variabel

modell = LinearRegression()
modell.fit(x, y)

# Prediksjon
x_ny = np.array([6]).reshape(-1, 1)
y_predikert = modell.predict(x_ny)
print("Predikert verdi for x = 6:", y_predikert)

# Visualisering
plt.scatter(x, y, color='blue')
plt.plot(x, modell.predict(x), color='red')
plt.title('Lineær regresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.show()