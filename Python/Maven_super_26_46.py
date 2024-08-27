python
import csv

data = [
    ['Navn', 'Alder', 'By'],
    ['Anna', 23, 'Oslo'],
    ['Bob', 35, 'Bergen'],
    ['Charlie', 30, 'Trondheim']
]

with open('utdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
    skriver = csv.writer(csvfile)
    skriver.writerows(data)