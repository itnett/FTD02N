python
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user['id'] == user_id:
            user['name'] = data.get('name', user['name'])
            user['email'] = data.get('email', user['email'])
            return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)