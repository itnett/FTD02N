python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("kampanjeresultater.csv")
sns.barplot(x='Kampanje', y='Resultat', data=data)
plt.title("Kampanjeresultater")
plt.show()