python
import csv

data = [
    ['Navn', 'Alder', 'By'],
    ['Alice', '30', 'Oslo'],
    ['Bob', '25', 'Bergen']
]

with open('data.csv', 'w', newline='') as fil:
    writer = csv.writer(fil)
    writer.writerows(data)