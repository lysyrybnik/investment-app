from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

# 🔑 Wstaw tutaj swoje klucze API!
POLYGON_API_KEY = "xYEuuBe9Tls4WaIm4J5_RDxo2fXrFK1I"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Pobieranie cen akcji
@app.route("/stocks", methods=["GET"])
def get_stock_prices():
    symbol = request.args.get("symbol", "AAPL")
    url = f"https://api.polygon.io/v2/last/trade/{symbol}"
    headers = {"Authorization": f"Bearer {POLYGON_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return jsonify(data)

# Pobieranie newsów giełdowych
@app.route("/news", methods=["GET"])
def get_stock_news():
    symbol = request.args.get("symbol", "AAPL")
    url = f"https://api.polygon.io/v2/reference/news?ticker={symbol}"
    headers = {"Authorization": f"Bearer {POLYGON_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
