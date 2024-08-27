python
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

API_KEY = "minhemmeligeapi-nøkkel"

def check_api_key():
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        abort(401)

@app.route('/books', methods=['GET'])
def get_books():
    check_api_key()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    check_api_key()
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)