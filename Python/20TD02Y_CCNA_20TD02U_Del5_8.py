python
   from flask import Flask, jsonify, request

   app = Flask(__name__)

   users = [
       {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
       {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
   ]

   @app.route('/users', methods=['GET'])
   def get_users():
       return jsonify(users)

   @app.route('/users', methods=['POST'])
   def create_user():
       new_user = request.get_json()
       users.append(new_user)
       return jsonify(new_user), 201

   @app.route('/users/<int:user_id>', methods=['PUT'])
   def update_user(user_id):
       updated_user = request.get_json()
       for user in users:
           if user['id'] == user_id:
               user.update(updated_user)
               return jsonify(user)
       return jsonify({'message': 'User not found'}), 404

   @app.route('/users/<int:user_id>', methods=['DELETE'])
   def delete_user(user_id):
       global users
       users = [user for user in users if user['id'] != user_id]
       return '', 204

   if __name__ == '__main__':
       app.run(debug=True)