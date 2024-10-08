python
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}])

if __name__ == '__main__':
    app.run(debug=True)