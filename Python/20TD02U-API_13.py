python
from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/users', methods=['GET'])
@cache.cached(timeout=60)
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)