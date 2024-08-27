python
import json

# Skrive data til en JSON-fil
data = {"navn": "Anna", "alder": 25, "by": "Oslo"}
with open("data.json", "w") as fil:
    json.dump(data, fil)

# Lese data fra en JSON-fil
with open("data.json", "r") as fil:
    data = json.load(fil)
    print(data)