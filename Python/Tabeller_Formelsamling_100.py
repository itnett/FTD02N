python
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import plotly.express as px

# Last inn data
df = sns.load_dataset('iris')

# Utforsk data
print(df.head())

# Visualiser data
sns.pairplot(df, hue='species')
plt.show()

# Forbered data for maskinlæring
X = df.drop(columns=['species'])
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Tren modellen
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Prediksjon
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Interaktiv visualisering med Plotly
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                 title="Iris Dataset - Sepal Width vs Sepal Length")
fig.show()