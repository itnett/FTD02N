python
import requests
import numpy as np
import pandas as pd

# Bruk av requests for å hente data fra nettet
response = requests.get('https://api.github.com')
print(response.json())

# Bruk av numpy for å skape og manipulere matriser
array = np.array([1, 2, 3, 4])
print(array.mean())  # Utskrift: Gjennomsnittet av elementene

# Bruk av pandas for å lage og manipulere dataframes
data = {
    "navn": ["Anna", "Bob", "Charlie"],
    "alder": [23, 35, 30]
}
df = pd.DataFrame(data)
print(df)