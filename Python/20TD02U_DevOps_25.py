python
   from sklearn.ensemble import RandomForestClassifier
   import pandas as pd

   # Last inn data
   data = pd.read_csv('metrics.csv')

   # Forbered data for modelltrening
   X = data.drop('failure', axis=1)
   y = data['failure']

   # Tren en prediktiv modell
   model = RandomForestClassifier()
   model.fit(X, y)

   # Bruk modellen til å forutsi feil
   predictions = model.predict(new_data)