from flask import Flask, render_template, request, jsonify
from vnstock.explorer.fmarket.fund import Fund

app = Flask(__name__)
fund = Fund()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/top_holdings')
def top_holdings():
    symbol = request.args.get('symbol', 'SSISCA')
    df = fund.details.top_holding(symbol)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
