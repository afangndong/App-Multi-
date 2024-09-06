from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/products', methods=['GET'])
def get_articles():
    articles = [
        {"id": 1, "title": "Product 1", "content": "Content of Product 1"},
        {"id": 2, "title": "Product 2", "content": "Content of Product 2"},
    ]
    return jsonify(articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)