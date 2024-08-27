python
from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'}
]

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify(new_item), 201

@app.route('/data/<int:item_id>', methods=['PUT'])
def update_data(item_id):
    updated_item = request.get_json()
    for item in data:
        if item['id'] == item_id:
            item.update(updated_item)
            return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

@app.route('/data/<int:item_id>', methods=['DELETE'])
def delete_data(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)