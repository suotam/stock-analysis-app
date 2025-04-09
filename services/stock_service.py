import requests
import json
from models.stock import Stock
import yfinance as yf
import pandas as pd
import os

def get_stock_price(stock_name):
    try:
        stock = yf.Ticker(stock_name)
        data = stock.history(period="1d")  # Získáme historická data za 1 den
        if not data.empty:
            price = data['Close'].iloc[-1]  # Získáme poslední cenu (Close price)
            volume = data['Volume'].iloc[-1]  # Získáme objem akcií
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
        # Převedeme všechna čísla na float pro správnou serializaci
        json.dump([{
            'name': stock.name,
            'price': float(stock.price) if isinstance(stock.price, (int, float)) else float(stock.price),
            'volume': float(stock.volume) if isinstance(stock.volume, (int, float)) else float(stock.volume)
        } for stock in stocks], f, indent=4)

def load_stocks_from_json(filename='data/stocks_data.json'):
    """ Načte seznam akcií z JSON souboru, nebo vytvoří soubor pokud neexistuje """
    if not os.path.exists(filename):  # Kontrola, zda soubor existuje
        print(f"Soubor {filename} neexistuje. Vytváříme nový soubor.")
        # Pokud soubor neexistuje, vytvoříme ho s prázdným seznamem
        save_stocks_to_json([])  # Uloží prázdný seznam do souboru
        return []
    
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Stock(**item) for item in data]
    except json.JSONDecodeError:  # Pokud je soubor poškozený nebo nevalidní JSON
        print(f"Chyba při čtení souboru {filename}. Soubor bude přeformátován.")
        return []  # Vrátíme prázdný seznam v případě chyby