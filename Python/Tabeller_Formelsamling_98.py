python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Last inn data
iris = load_iris()
X, y = iris.data, iris.target

# Del data i treningssett og testsett
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Tren modellen
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Prediksjon
y_pred = model.predict(X_test)

# Evaluer modellens nøyaktighet
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")