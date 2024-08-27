python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}])

if __name__ == '__main__':
    app.run(port=5000)