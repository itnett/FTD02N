python
import csv
import json

# Les fra en CSV-fil
csv_file = 'data.csv'
json_file = 'data.json'

data = []
with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

# Skriv data til en JSON-fil
with open(json_file, mode='w') as file:
    json.dump(data, file, indent=4)

print(f"Data konvertert fra {csv_file} til {json_file}")