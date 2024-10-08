python
import csv

sårbarheter = [
    {"navn": "CVE-2023-1234", "alvorlighetsgrad": "høy", "system": "webserver1"},
    {"navn": "CVE-2023-5678", "alvorlighetsgrad": "middels", "system": "dbserver1"},
]

with open("sårbarhetsrapport.csv", "w", newline="") as csvfile:
    feltnavn = ["navn", "alvorlighetsgrad", "system"]
    skriver = csv.DictWriter(csvfile, fieldnames=feltnavn)
    skriver.writeheader()
    for sårbarhet in sårbarheter:
        skriver.writerow(sårbarhet)