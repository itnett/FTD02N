python
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

data = pd.read_csv("salg

.csv", index_col='Dato', parse_dates=True)
model = ExponentialSmoothing(data['Salg'], seasonal='add', seasonal_periods=12).fit()
prognoser = model.forecast(12)

data['Salg'].plot(label='Historisk Salg')
prognoser.plot(label='Prognose')
plt.legend()
plt.show()