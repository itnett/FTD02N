python
sårbarheter = [
    {"navn": "CVE-2023-1234", "alvorlighetsgrad": "høy"},
    {"navn": "CVE-2023-5678", "alvorlighetsgrad": "middels"},
    {"navn": "CVE-2023-9012", "alvorlighetsgrad": "lav"},
]

# Sorter sårbarhetene etter alvorlighetsgrad (synkende)
sårbarheter.sort(key=lambda x: x["alvorlighetsgrad"], reverse=True)

# Legg til en ny sårbarhet
sårbarheter.append({"navn": "CVE-2023-3456", "alvorlighetsgrad": "kritisk"})

print(sårbarheter)