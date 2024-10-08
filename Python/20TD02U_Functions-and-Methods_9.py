python
   def clean_data(df):
       """
       Clean the DataFrame by filling missing values.
       :param df: DataFrame
       :return: DataFrame
       """
       df.fillna(0, inplace=True)
       return df