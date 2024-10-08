python
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/users', methods=['GET'])
@limiter.limit("10 per minute")
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)