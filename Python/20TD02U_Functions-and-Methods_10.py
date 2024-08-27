python
   def analyze_data(df):
       """
       Perform data analysis by calculating summary statistics.
       :param df: DataFrame
       :return: dict
       """
       summary = {
           'mean': df.mean(),
           'median': df.median(),
           'std': df.std()
       }
       return summary