python
data = [["navn", "alder", "epost"], ["Alice", "30", "alice@eksempel.no"], ["Bob", "25", "bob@eksempel.no"]]

csv_strenger = []
for rad in data:
    csv_strenger.append(",".join(rad))

csv_innhold = "\n".join(csv_strenger)
print(csv_innhold)