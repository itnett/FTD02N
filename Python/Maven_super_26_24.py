python
from flask import Flask, jsonify, request

app = Flask(__name__)

bøker = [
    {"id": 1, "tittel": "Python for alle", "forfatter": "John Smith"},
    {"id": 2, "tittel": "Lære Flask", "forfatter": "Jane Doe"},
]

# Endepunkt for å hente alle bøker
@app.route('/bøker', methods=['GET'])
def get_bøker():
    return jsonify(bøker)

# Endepunkt for å legge til en ny bok
@app.route('/bøker', methods=['POST'])
def add_bok():
    ny_bok = request.json
    bøker.append(ny_bok)
    return jsonify(ny_bok), 201

# Endepunkt for å fjerne en bok basert på ID
@app.route('/bøker/<int:id>', methods=['DELETE'])
def delete_bok(id):
    bok = next((bok for bok in bøker if bok["id"] == id), None)
    if bok:
        bøker.remove(bok)
        return jsonify(bok)
    else:
        return jsonify({"error": "Bok ikke funnet"}), 404

if __name__ == '__main__':
    app.run(debug=True)