python
    sales_data = {"Q1": 20000, "Q2": 30000, "Q3": 25000, "Q4": 40000}

    plt.plot(sales_data.keys(), sales_data.values(), marker='o')
    plt.title('Kvartalsvis Salgsanalyse')
    plt.xlabel('Kvartaler')
    plt.ylabel('Salg (NOK)')
    plt.show()