python
import csv

with open('data.csv', newline='', encoding='utf-8') as csvfile:
    leser = csv.reader(csvfile)
    for rad in leser:
        print(rad)