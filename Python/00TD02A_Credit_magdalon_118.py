python
import json

# JSON-objekt
person_json = '{"navn": "Alice", "alder": 30, "by": "Oslo"}'

# Konverter JSON til Python-ordbok
person_dict = json.loads(person_json)
print(person_dict["navn"])  # Output: Alice

# Python-ordbok
konfigurasjon = {
    "server_navn": "webserver1",
    "port": 80,
    "ssl_aktivert": True,
}

# Konverter Python-ordbok til JSON
konfigurasjon_json = json.dumps(konfigurasjon)
print(konfigurasjon_json)  # Output: {"server_navn": "webserver1", "port": 80, "ssl_aktivert": true}