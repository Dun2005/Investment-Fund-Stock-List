from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Danh sách mã cổ phiếu giả định của quỹ VFMVN30
portfolio = {
    "VFMVN30": ["FPT", "VNM", "VCB", "MWG", "HPG"]
}

# Lấy giá từ API miễn phí
def get_stock_price(ticker):
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}.VN"
    response = requests.get(url)
    try:
        data = response.json()
        return data['quoteResponse']['result'][0]['regularMarketPrice']
        
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
        print("Response content:", response.text[:200])
        return None

@app.route('/fund/<fund_name>')
def get_fund(fund_name):
    tickers = portfolio.get(fund_name.upper())
    if not tickers:
        return jsonify({"error": "Quỹ không tồn tại"}), 404
    
    result = []
    for ticker in tickers:
        price = get_stock_price(ticker)
        result.append({"ticker": ticker, "price": price})
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)