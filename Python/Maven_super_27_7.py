python
    import pandas as pd

    data = pd.read_csv('stor_fil.csv')
    filtrert_data = data[data['kolonne'] > 1000]