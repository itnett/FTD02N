python
import matplotlib.pyplot as plt
import pandas as pd

data = {'A': [0, 0, 1, 1],
        'B': [0, 1, 0, 1]}
df = pd.DataFrame(data)
df['A AND B'] = df['A'] & df['B']
df['A OR B'] = df['A'] | df['B']
df['NOT A'] = ~df['A']

fig, ax = plt.subplots(1, 1, figsize=(10, 2))
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
plt.show()