python
import csv

with open("loggfil.csv", "r", newline="") as csvfile:
    leser = csv.reader(csvfile, delimiter=",")
    for rad in leser:
        print(rad)