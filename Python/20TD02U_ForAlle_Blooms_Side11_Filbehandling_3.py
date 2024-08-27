python
import csv

with open('data.csv', 'r') as fil:
    reader = csv.reader(fil)
    for rad in reader:
        print(rad)