python
import json

konfigurasjon = {
    "brannmur": {
        "regler": [
            {"protokoll": "tcp", "port": 80, "handling": "tillat"},
            {"protokoll": "tcp", "port": 443, "handling": "tillat"},
            {"protokoll": "udp", "port": 53, "handling": "tillat"},
        ]
    },
    "inntrengingsdeteksjon": {
        "aktivert": True,
        "logg_nivå": "detaljert",
    },
}

# Lagre konfigurasjonen til en JSON-fil
with open("sikkerhet_config.json", "w") as f:
    json.dump(konfigurasjon, f, indent=4)