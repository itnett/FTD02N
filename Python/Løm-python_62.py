python
    import pandas as pd

    data = {
        'Type': ['Inntekter', 'Utgifter'],
        'Beløp': [500000, 350000]
    }

    regnskap = pd.DataFrame(data)
    print(regnskap)