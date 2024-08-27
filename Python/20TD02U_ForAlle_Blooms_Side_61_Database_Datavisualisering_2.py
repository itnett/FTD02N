python
import seaborn as sns
import matplotlib.pyplot as plt

# Eksempeldata
tips = sns.load_dataset('tips')

# Lage et scatter plot med fargekoding
sns.scatterplot(x='total_bill', y='tip', hue='day', data=tips)
plt.title('Sammenheng mellom total regning og tips med fargekoding etter dag')
plt.show()