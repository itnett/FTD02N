python
   import matplotlib.pyplot as plt

   def visualize_data(df):
       """
       Create a bar plot of the DataFrame.
       :param df: DataFrame
       """
       df.plot(kind='bar')
       plt.show()