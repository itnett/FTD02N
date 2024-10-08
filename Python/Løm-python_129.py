python
import pandas as pd

# Simulert data for klager
data = {
    'Kunde': ['Kunde A', 'Kunde B', 'Kunde C', 'Kunde D'],
    'Klager': ['Favorisering', 'Feil fakturering', 'Dårlig kommunikasjon', 'Feil fakturering'],
    'Antall': [1, 3, 2, 1]
}

df = pd.DataFrame(data)

# Analysering av klager
klager_gruppert = df.groupby('Klager').sum()

print("Antall klager per kategori:")
print(klager_gruppert)