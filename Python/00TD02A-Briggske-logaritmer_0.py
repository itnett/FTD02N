python
import matplotlib.pyplot as plt
import pandas as pd

data = {'Number': [1, 10, 100, 1000, 10000],
        'Logarithm (Base 10)': [0, 1, 2, 3, 4]}
df = pd.DataFrame(data)

fig, ax = plt.subplots(1, 1, figsize=(10, 2))
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
plt.show()