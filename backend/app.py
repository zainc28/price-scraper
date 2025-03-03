from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Price Scraper API!"

@app.route('/api/products/search', methods=['GET'])
def search_products():
    query = request.args.get('query')  # Get the search query from the URL
    if not query:
        return jsonify({"error": "Please provide a search query."}), 400

    # Example: Scrape eBay for the product
    try:
        url = f"https://www.ebay.com/sch/{query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        print(response.text)

        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.find_all('div', {'class': 's-item__info'}):
            name = item.find('div', {'class': 's-item__title'})
            price = item.find('span', {'class': 's-item__price'})
            if name and price:
                products.append({
                    "name": name.text.strip(),
                    "price": price.text.strip(),
                    "website": "eBay"
                })

        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)