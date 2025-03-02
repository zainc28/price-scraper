from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Price Scraper API!"

@app.route('/api/products/search', methods=['GET'])
def search_products():
    return jsonify({"message": "This will return search results in the future."})

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)