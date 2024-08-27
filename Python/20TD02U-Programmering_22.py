python
# Python - Flask API eksempel
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"data": "value"})

if __name__ == '__main__':
    app.run()