python
import pandas as pd

def analyze_data(file_path):
    """
    Analyserer data fra en fil ved hjelp av pandas.

    Parametere:
    file_path (str): Stien til filen som skal analyseres

    Returnerer:
    pd.DataFrame: Analysert data
    """
    df = pd.read_csv(file_path)
    summary = df.describe()
    return summary

# Eksempel på bruk
# summary = analyze_data("/path/to/datafile.csv")
# print(summary)