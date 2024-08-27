python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generer data fra en normalfordeling
data = np.random.normal(loc=180, scale=6, size=10000)

# Tegn histogrammet
sns.histplot(data, kde=True)
plt.title("Normalfordeling med gjennomsnitt 180 og standardavvik 6")
plt.xlabel("Verdi")
plt.ylabel("Frekvens")
plt.show()