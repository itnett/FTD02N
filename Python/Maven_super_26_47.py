python
import json

with open('data.json', 'r', encoding='utf-8') as fil:
    data = json.load(fil)
    print(data)