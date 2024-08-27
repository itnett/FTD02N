python
import json

data = {"navn": "Alice", "alder": 30}

# Serialisering
with open("data.json", "w") as f:
    json.dump(data, f)

# Deserialisering
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)