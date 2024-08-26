from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question', '').lower()

    if "stock" in question:
        stock_symbol = question.split('stock ')[-1].upper()
        try:
            stock = yf.Ticker(stock_symbol)
            info = stock.info
            response = {
                'name': info.get('shortName', 'N/A'),
                'price': info.get('currentPrice', 'N/A'),
                'details': info.get('longBusinessSummary', 'N/A')
            }
        except Exception as e:
            response = {'response': f"Error fetching data: {str(e)}"}
        return jsonify(response)

    return jsonify({'response': "Sorry, I can't help with that question."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
