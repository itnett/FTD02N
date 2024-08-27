python
import json

data = {
    'navn': 'Alice',
    'alder': 30,
    'by': 'Oslo'
}

with open('data.json', 'w') as fil:
    json.dump(data, fil, indent=4)