python
from flask import Flask, request, jsonify

app = Flask(__name__)

brukere = {}

@app.route('/bruker', methods=['POST'])
def legg_til_bruker():
    data = request.get_json()
    brukernavn = data['navn']
    brukere[brukernavn] = data
    return jsonify({"message": "Bruker lagt til"}), 201

@app.route('/bruker/<navn>', methods=['GET'])
def hent_bruker(navn):
    return jsonify(brukere.get(navn, "Bruker ikke funnet")), 200

if __name__ == '__main__':
    app.run(debug=True)