python
import logging
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/users', methods=['GET'])
def get_users():
    app.logger.info("GET /users")
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)