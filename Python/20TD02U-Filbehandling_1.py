python
import csv

with open("data.csv", "r") as f:
    leser = csv.reader(f)
    for rad in leser:
        print(rad)