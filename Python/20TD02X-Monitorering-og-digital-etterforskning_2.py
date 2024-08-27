python
    import pandas as pd
    import matplotlib.pyplot as plt

    # Les inn loggdata fra en CSV-fil
    logs = pd.read_csv('logs.csv')

    # Analyser dataene for å finne antall hendelser per type
    event_counts = logs['event_type'].value_counts()

    # Visualiser resultatene i et stolpediagram
    plt.figure(figsize=(10, 6))
    event_counts.plot(kind='bar')
    plt.title('Antall sikkerhetshendelser per type')
    plt.xlabel('Hendelsestype')
    plt.ylabel('Antall')
    plt.show()