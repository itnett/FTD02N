python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Simulert datamengde (i GB) over tid (i timer)
time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
data = np.array([50, 55, 53, 60, 65, 63, 70, 75, 78, 80])

# Tren regresjonsmodellen
model = LinearRegression()
model.fit(time, data)

# Forutsi fremtidig trafikk
future_time = np.array([11, 12, 13, 14, 15]).reshape(-1, 1)
predicted_data = model.predict(future_time)

# Plot resultatene
plt.plot(time, data, 'bo-', label='Historical Data')
plt.plot(future_time, predicted_data, 'r--', label='Predicted Data')
plt.xlabel('Time (hours)')
plt.ylabel('Data (GB)')
plt.title('Network Traffic Prediction')
plt.legend()
plt.show()