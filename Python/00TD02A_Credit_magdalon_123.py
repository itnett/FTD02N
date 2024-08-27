python
import csv

with open("output.csv", "w", newline="") as csvfile:
    skriver = csv.writer(csvfile, delimiter=",")
    skriver.writerow(["Navn", "Alder", "Epost"])
    skriver.writerow(["Alice", 30, "alice@eksempel.no"])
    skriver.writerow(["Bob", 25, "bob@eksempel.no"])