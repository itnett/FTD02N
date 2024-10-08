python
   import pandas as pd

   def load_data(file_path):
       """
       Load data from a CSV file.
       :param file_path: str
       :return: DataFrame
       """
       return pd.read_csv(file_path)