python
# Risikoanalyse
risikoer = [
    {"navn": "Datainnbrudd", "sannsynlighet": 0.7, "konsekvens": 9},
    {"navn": "Tjenestenektangrep", "sannsynlighet": 0.5, "konsekvens": 7},
    {"navn": "Intern feilhåndtering", "sannsynlighet": 0.3, "konsekvens": 5}
]

for risiko in risikoer:
    risiko["risiko_score"] = risiko["sannsynlighet"] * risiko["konsekvens"]

# Sorter risikoer etter risiko_score
risikoer.sort(key=lambda x: x["risiko_score"], reverse=True)

for risiko in risikoer:
    print(f"Risiko: {risiko['navn']}, Score: {risiko['risiko_score']}")