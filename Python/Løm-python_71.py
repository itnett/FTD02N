python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('økonomiske_data.csv')
data.plot(x='År', y=['Inntekter', 'Utgifter'], kind='line')
plt.show()