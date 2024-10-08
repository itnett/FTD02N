python
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns

   # Last inn sosiale medier-data
   data = pd.read_csv("sosiale_medier.csv")

   # Analyser engasjement og rekkevidde
   engasjement = data.groupby('PostType')['Likes', 'Shares', 'Comments'].sum()

   # Visualiser dataene
   engasjement.plot(kind='bar', stacked=True)
   plt.title("Engasjement per Post Type")
   plt.xlabel("Post Type")
   plt.ylabel("Engasjement")
   plt.show()