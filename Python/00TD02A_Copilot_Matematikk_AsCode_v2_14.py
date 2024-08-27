python
import numpy as np
from sklearn.linear_model import LinearRegression

# Eksempeldata
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 3, 5, 7, 11])

# Tren modell
model = LinearRegression()
model.fit(x, y)

# Prediksjoner
predictions = model.predict(x)
predictions