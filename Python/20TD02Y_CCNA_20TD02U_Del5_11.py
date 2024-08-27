python
   from flask import Flask, jsonify, request
   from flask_cors import CORS
   from flask_limiter import Limiter
   from flask_caching import Cache
   from flask_graphql import GraphQLView
   import graphene

   app = Flask(__name__)
   CORS(app)
   limiter = Limiter(app, default_limits=["200 per day", "50 per hour"])
   cache = Cache(app, config={'CACHE_TYPE': 'simple'})

   users = [
       {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
       {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
   ]

   @app.route('/users', methods=['GET'])
   @limiter.limit("10 per minute")
   @cache.cached(timeout=60)
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

   class User(graphene.ObjectType):
       id = graphene.Int()
       name = graphene.String()
       email = graphene.String()

   class Query(graphene.ObjectType):
       users = graphene.List(User)

       def resolve_users(self, info):
           return users

   schema = graphene.Schema(query=Query)
   app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

   if __name__ == '__main__':
       app.run(debug=True)