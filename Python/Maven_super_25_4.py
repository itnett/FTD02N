python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Enkle data for lagring av bøker
books = []

# API-endepunkt for å hente listen over bøker
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# API-endepunkt for å legge til en ny bok
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201

# API-endepunkt for å fjerne en bok
@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    if 0 <= index < len(books):
        removed_book = books.pop(index)
        return jsonify(removed_book)
    else:
        return jsonify({"error": "Bok ikke funnet"}), 404

# Kjører Flask-serveren
if __name__ == '__main__':
    app.run(debug=True)