from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/payments', methods=['GET'])
def get_payments():
    payments = [
        {"id": 1, "amount": 100, "status": "Completed"},
        {"id": 2, "amount": 200, "status": "Pending"},
    ]
    return jsonify(payments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)