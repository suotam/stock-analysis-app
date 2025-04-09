import requests
import json
from models.crypto import Crypto

def get_crypto_price(crypto_name):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    if crypto_name in data:
        return data[crypto_name]['usd']
    else:
        print(f"Chyba při získávání dat pro {crypto_name}")
        return None

def update_crypto_data(crypto):
    price = get_crypto_price(crypto.name)
    if price:
        crypto.price = price

def save_cryptos_to_json(cryptos, filename='data/cryptos_data.json'):
    """ Uloží seznam kryptoměn do JSON souboru """
    with open(filename, 'w') as f:
        json.dump([crypto.__dict__ for crypto in cryptos], f, indent=4)

def load_cryptos_from_json(filename='data/cryptos_data.json'):
    """ Načte seznam kryptoměn z JSON souboru """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Crypto(**item) for item in data]
    except FileNotFoundError:
        print(f"Soubor {filename} neexistuje.")
        return []