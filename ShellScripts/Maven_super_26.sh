bash
# Hente alle bøker
curl -X GET http://127.0.0.1:5000/bøker

# Legge til en ny bok
curl -X POST -H "Content-Type: application/json" -d '{"id": 3, "tittel": "Lær APIer", "forfatter": "Mary Jane"}' http://127.0.0.1:5000/bøker

# Slette en bok basert på ID
curl -X DELETE http://127.0.0.1:5000/bøker/3