import json
from models.stock import Stock

def load_stocks():
    with open('data/stocks.json', 'r') as file:
        stock_data = json.load(file)
    stocks = []
    for data in stock_data:
        stock = Stock(data['name'], data['price'], data['volume'])
        stocks.append(stock)
    return stocks

stocks = load_stocks()
for stock in stocks:
    stock.print_info()