python
import pandas as pd
import matplotlib.pyplot as plt

# Sample data fra en undersøkelse
data = {
    'Tid (dager)': [0, 1, 2, 3, 4, 5, 6, 7],
    'Bakterier (cfu)': [100, 150, 225, 337, 505, 757, 1135, 1703]
}

df = pd.DataFrame(data)

# Plot dataene
plt.figure(figsize=(10, 6))
plt.plot(df['Tid (dager)'], df['Bakterier (cfu)'], marker='o')
plt.xlabel('Tid (dager)')
plt.ylabel('Bakterier (cfu)')
plt.title('Bakterievekst over tid')
plt.grid(True)
plt.show()

# Beregn gjennomsnittlig vekstrate per dag
df['Vekstrate per dag'] = df['Bakterier (cfu)'].pct_change() * 100
gjennomsnittlig_vekstrate = df['Vekstrate per dag'].mean()
print(f"Gjennomsnittlig vekstrate per dag: {gjennomsnittlig_vekstrate:.2f}%")