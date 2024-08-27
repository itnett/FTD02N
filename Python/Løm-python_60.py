python
    import pandas as pd

    data = {
        'Måned': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Inntekter': [20000, 22000, 21000, 23000],
        'Utgifter': [15000, 16000, 17000, 18000]
    }

    df = pd.DataFrame(data)
    df['Resultat'] = df['Inntekter'] - df['Utgifter']
    print(df)