python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Last inn datasett (simulert eksempel)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Energy_Consumption_kWh': [3000, 2800, 3200, 3500, 4000, 4500, 4700, 4600, 4200, 3800, 3400, 3100]
}
df = pd.DataFrame(data)

# Kalkuler gjennomsnittlig energiforbruk
average_consumption = df['Energy_Consumption_kWh'].mean()
print(f"Gjennomsnittlig energiforbruk: {average_consumption} kWh")

# Identifiser måned med høyest energiforbruk
max_consumption = df['Energy_Consumption_kWh'].max()
max_month = df[df['Energy_Consumption_kWh'] == max_consumption]['Month'].values[0]
print(f"Høyest energiforbruk er i {max_month} med {max_consumption} kWh")

# Plot energiforbruket
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Energy_Consumption_kWh'], marker='o')
plt.title('Energiforbruk per Måned')
plt.xlabel('Måned')
plt.ylabel('Energi (kWh)')
plt.grid(True)
plt.show()

# Foreslå energisparingstiltak basert på data
def forslag_tiltak(consumption):
    if consumption > average_consumption:
        return "Foreslå energibesparende tiltak som forbedret isolasjon eller effektiv belysning."
    else:
        return "Energiforbruket er under gjennomsnittet. Fortsett med gode praksiser."

df['Tiltak'] = df['Energy_Consumption_kWh'].apply(forslag_tiltak)
print(df)