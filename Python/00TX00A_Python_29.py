python
import pandas as pd

def create_spreadsheet():
    """
    Create a spreadsheet for financial data.
    """
    data = {
        'Måned': ['Januar', 'Februar', 'Mars'],
        'Inntekter': [20000, 25000, 30000],
        'Kostnader': [15000, 16000, 17000],
        'Resultat': [5000, 9000, 13000]
    }
    df = pd.DataFrame(data)
    df.to_excel("/mnt/data/financial_data.xlsx", index=False)
    print("Spreadsheet saved as 'financial_data.xlsx'")

# Eksempel på bruk
create_spreadsheet()