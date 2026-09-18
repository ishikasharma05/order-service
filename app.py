from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def health():
    return jsonify(status="ok", service="order-service", env=os.getenv("ENVIRONMENT", "dev"))

@app.route('/orders')
def orders():
    return jsonify(orders=[{"id": 101, "item": "Laptop", "status": "shipped"}, {"id": 102, "item": "Mouse", "status": "pending"}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
