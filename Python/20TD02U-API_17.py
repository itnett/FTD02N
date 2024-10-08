python
from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return [
            User(id=1, name="Ola Nordmann", email="ola@example.com"),
            User(id=2, name="Kari Nordmann", email="kari@example.com")
        ]

schema = graphene.Schema(query=Query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)