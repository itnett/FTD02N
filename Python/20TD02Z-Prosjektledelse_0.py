python
    import pandas as pd

    risks = pd.DataFrame({
        'Risiko': ['Forsinket levering', 'Budsjettoverskridelse', 'Tekniske problemer'],
        'Sannsynlighet': [0.3, 0.2, 0.4],
        'Konsekvens': [0.8, 0.6, 0.7]
    })

    risks['Risikoscore'] = risks['Sannsynlighet'] * risks['Konsekvens']
    print(risks)