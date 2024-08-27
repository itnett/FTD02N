python
import json

data = {
    "navn": "Anna",
    "alder": 23,
    "by": "Oslo"
}

with open('utdata.json', 'w', encoding='utf-8') as fil:
    json.dump(data, fil, indent=4)