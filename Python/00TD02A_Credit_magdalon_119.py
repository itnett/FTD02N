python
import requests
import json

api_url = "https://api.example.com/sårbarheter"
respons = requests.get(api_url)
sårbarheter = json.loads(respons.text)

# Analyser sårbarhetsdataene
for sårbarhet in sårbarheter:
    print(f"CVE: {sårbarhet['cve']}, Alvorlighetsgrad: {sårbarhet['alvorlighetsgrad']}")