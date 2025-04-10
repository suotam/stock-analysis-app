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


def add_new_crypto(crypto_name):
    price = get_crypto_price(crypto_name)
    if price:
        new_crypto = Crypto(name=crypto_name, price=price)
        
        cryptos = load_cryptos_from_json()
        
        cryptos.append(new_crypto)
        
        save_cryptos_to_json(cryptos)
        print(f"Kryptoměna {crypto_name} byla úspěšně přidána.")
    else:
        print(f"Chyba při přidávání kryptoměny {crypto_name}.")

def remove_crypto_from_json(crypto_name, filename='data/cryptos_data.json'):
    """ Smaže kryptoměnu z JSON souboru """
    cryptos = load_cryptos_from_json(filename)
    cryptos_to_keep = [crypto for crypto in cryptos if crypto.name != crypto_name]
    if len(cryptos_to_keep) == len(cryptos):
        print(f"Kryptoměna {crypto_name} nebyla nalezena.")
    else:
        save_cryptos_to_json(cryptos_to_keep, filename)
        print(f"Kryptoměna {crypto_name} byla úspěšně odstraněna.")

def update_crypto(crypto):
    """Aktualizuje data pro jednu kryptoměnu"""
    price = get_crypto_price(crypto.name)
    if price:
        crypto.price = price
        print(f"Kryptoměna {crypto.name} byla úspěšně aktualizována.")
    else:
        print(f"Chyba při aktualizaci kryptoměny {crypto.name}.")

def update_all_cryptos():
    """Aktualizuje data pro všechny kryptoměny"""
    cryptos = load_cryptos_from_json()
    for crypto in cryptos:
        update_crypto_data_for_one(crypto)
    save_cryptos_to_json(cryptos)
    print("Všechny kryptoměny byly úspěšně aktualizovány.")