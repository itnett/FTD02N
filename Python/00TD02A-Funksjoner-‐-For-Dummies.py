python
# Trinket-kode for Leksjon 5: Regresjon ved hjelp av digitale hjelpemidler

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Eksempeldata: {(1, 2), (2, 3), (3, 5), (4, 7)}
x_values = np.array([1, 2, 3, 4]).reshape((-1, 1))
y_values = np.array([2, 3, 5, 7])

# Utfør lineær regresjon
model = LinearRegression()
model.fit(x_values, y_values)
y_pred = model.predict(x_values)

# Tegn dataene og den beste tilpassede linjen
plt.scatter(x_values, y_values, color='blue', label='Data points')
plt.plot(x_values, y_pred, color='red', label='Best fit line')
plt.title('Lineær Regresjon')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth

=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Numerisk output: ligningen for den beste tilpassede linjen
print(f"Ligningen for den beste tilpassede linjen: y = {model.coef_[0]}x + {model.intercept_}")