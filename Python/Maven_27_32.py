python
    import matplotlib.pyplot as plt

    # Eksempeldata
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    revenues = [10000, 15000, 12000, 18000]

    # Lage en enkel linjediagram
    plt.plot(categories, revenues, marker='o')
    plt.title('Kvartalsvis inntekt')
    plt.xlabel('Kvartaler')
    plt.ylabel('Inntekt (NOK)')
    plt.show()