python
import pandas as pd
import matplotlib.pyplot as plt

# Eksempeldata (tidsserie)
data = {
    'Dato': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Salg': [100, 150, 200, 250, 230, 220, 210, 260, 300, 320, 330, 350]
}
df = pd.DataFrame(data)

# Plotting av tidsserie
plt.plot(df['Dato'], df['Salg'])
plt.title('Salgsutvikling gjennom året')
plt.xlabel('Dato')
plt.ylabel('Salg')
plt.show()