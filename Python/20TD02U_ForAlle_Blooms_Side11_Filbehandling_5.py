python
import json

with open('data.json', 'r') as fil:
    data = json.load(fil)
    print(data)