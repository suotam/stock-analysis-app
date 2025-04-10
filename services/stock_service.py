import requests
import json
from models.stock import Stock
import yfinance as yf
import pandas as pd
import os

def get_stock_price(stock_name):
    try:
        stock = yf.Ticker(stock_name)
        data = stock.history(period="1d")  
        if not data.empty:
            price = data['Close'].iloc[-1] 
            volume = data['Volume'].iloc[-1]  
            return price, volume
        else:
            print(f"Chyba při získávání dat pro {stock_name}")
            return None, None
    except Exception as e:
        print(f"Chyba při získávání dat pro {stock_name}: {e}")
        return None, None

def update_stock_data(stock):
    price, volume = get_stock_price(stock.name)
    if price and volume:
        stock.price = price
        stock.volume = volume
    else:
        print(f"Data pro {stock.name} nebyla úspěšně načtena.")

def save_stocks_to_json(stocks, filename='data/stocks_data.json'):
    """ Uloží seznam akcií do JSON souboru """
    with open(filename, 'w') as f:
        json.dump([{
            'name': stock.name,
            'price': float(stock.price) if isinstance(stock.price, (int, float)) else float(stock.price),
            'volume': float(stock.volume) if isinstance(stock.volume, (int, float)) else float(stock.volume)
        } for stock in stocks], f, indent=4)

def load_stocks_from_json(filename='data/stocks_data.json'):
    """ Načte seznam akcií z JSON souboru, nebo vytvoří soubor pokud neexistuje """
    if not os.path.exists(filename):
        print(f"Soubor {filename} neexistuje. Vytváříme nový soubor.")
        save_stocks_to_json([])  
        return []
    
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Stock(**item) for item in data]
    except json.JSONDecodeError: 
        print(f"Chyba při čtení souboru {filename}. Soubor bude přeformátován.")
        return []  
    
def add_new_stock(stock_name):
    price, volume = get_stock_price(stock_name)
    if price and volume:
        new_stock = Stock(name=stock_name, price=price, volume=volume)
        
        stocks = load_stocks_from_json()
        
        stocks.append(new_stock)
        
        save_stocks_to_json(stocks)
        print(f"Akcie {stock_name} byla úspěšně přidána.")
    else:
        print(f"Chyba při přidávání akcie {stock_name}.")


def remove_stock_from_json(stock_name, filename='data/stocks_data.json'):
    """ Smaže akcii z JSON souboru """
    stocks = load_stocks_from_json(filename)
    stocks_to_keep = [stock for stock in stocks if stock.name != stock_name]
    if len(stocks_to_keep) == len(stocks):
        print(f"Akcie {stock_name} nebyla nalezena.")
    else:
        save_stocks_to_json(stocks_to_keep, filename)
        print(f"Akcie {stock_name} byla úspěšně odstraněna.")

def update_stock(stock):
    """Aktualizuje data pro jednu akcii"""
    price, volume = get_stock_price(stock.name)
    if price and volume:
        stock.price = price
        stock.volume = volume
        print(f"Akcie {stock.name} byla úspěšně aktualizována.")
    else:
        print(f"Chyba při aktualizaci akcie {stock.name}.")

def update_all_stocks():
    """Aktualizuje data pro všechny akcie"""
    stocks = load_stocks_from_json()
    for stock in stocks:
        update_stock_data_for_one(stock)
    save_stocks_to_json(stocks)
    print("Všechny akcie byly úspěšně aktualizovány.")