python
sårbarheter = [
    {"navn": "CVE-2023-1234", "alvorlighetsgrad": "høy", "system": "webserver1"},
    {"navn": "CVE-2023-5678", "alvorlighetsgrad": "middels", "system": "dbserver1"},
]

print("Sårbarhetsrapport:")
for sårbarhet in sårbarheter:
    print(f"- {sårbarhet['navn']} ({sårbarhet['alvorlighetsgrad']}): {sårbarhet['system']}")