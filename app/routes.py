from flask import Flask, jsonify, request
from app import app

# Dummy data for demonstration purposes
books = [
    {"id": 1, "title": "Flask 101", "author": "John Doe"},
    {"id": 2, "title": "Python Web Development", "author": "Jane Smith"}
]

# home
@app.route('/')
def home():
    return "HOME!!!"


# Endpoint to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Endpoint to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json.get('title'),
        "author": request.json.get('author')
    }
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)
