python
     # bibliotek_eksempler.py
     import numpy as np
     import pandas as pd
     import requests

     # NumPy example
     array = np.array([1, 2, 3, 4])
     print(f"NumPy array: {array}")
     print(f"Mean of array: {np.mean(array)}")

     # Pandas example
     data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
     df = pd.DataFrame(data)
     print("\nPandas DataFrame:")
     print(df)

     # Requests example
     response = requests.get('https://api.github.com')
     print(f"\nGitHub API response status: {response.status_code}")