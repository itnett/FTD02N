python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([{'order_id': 1, 'user_id': 1, 'amount': 100}, {'order_id': 2, 'user_id': 2, 'amount': 200}])

if __name__ == '__main__':
    app.run(port=5001)