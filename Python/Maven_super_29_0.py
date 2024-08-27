python
from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {"id": 1, "navn": "Anna", "alder": 25},
    {"id": 2, "navn": "Bob", "alder": 30}
]

@app.route('/personer', methods=['GET'])
def get_personer():
    return jsonify(data)

@app.route('/personer/<int:id>', methods=['GET'])
def get_person(id):
    person = next((p for p in data if p['id'] == id), None)
    return jsonify(person) if person else ('', 404)

@app.route('/personer', methods=['POST'])
def add_person():
    ny_person = request.json
    data.append(ny_person)
    return jsonify(ny_person), 201

@app.route('/personer/<int:id>', methods=['PUT'])
def update_person(id):
    person = next((p for p in data if p['id'] == id), None)
    if person:
        person.update(request.json)
        return jsonify(person)
    return ('', 404)

@app.route('/personer/<int:id>', methods=['DELETE'])
def delete_person(id):
    global data
    data = [p for p in data if p['id'] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)