python
    import matplotlib.pyplot as plt

    def market_analysis(data):
        for key, value in data.items():
            print(f"{key}: {value} kunder")

        plt.bar(data.keys(), data.values())
        plt.title('Markedsanalyse')
        plt.xlabel('Markedssegmenter')
        plt.ylabel('Antall kunder')
        plt.show()

    # Eksempeldata
    market_data = {"SMB": 120, "Enterprise": 80, "Freelancers": 50}
    market_analysis(market_data)