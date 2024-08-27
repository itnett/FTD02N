python
   import pandas as pd
   import seaborn as sns
   import matplotlib.pyplot as plt

   # Last inn medarbeiderundersøkelsesdata
   data = pd.read_csv("medarbeiderundersokelse.csv")

   # Analyser dataen, for eksempel medarbeidertilfredshet etter avdeling
   tilfredshet_per_avdeling = data.groupby('Avdeling')['Tilfredshet'].mean()

   # Visualiser resultatene
   sns.barplot(x=tilfredshet_per_avdeling.index, y=tilfredshet_per_avdeling.values)
   plt.title("Medarbeidertilfredshet per avdeling")
   plt.xlabel("Avdeling")
   plt.ylabel("Tilfredshet")
   plt.show()