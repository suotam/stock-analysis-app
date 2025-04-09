from models.crypto import Crypto
from services.crypto_service import update_crypto_data, save_cryptos_to_json, load_cryptos_from_json
from services.stock_service import update_stock_data, save_stocks_to_json, load_stocks_from_json

def load_data():
    cryptos = load_cryptos_from_json()  # Načteme kryptoměny z JSON
    stocks = load_stocks_from_json()   # Načteme akcie z JSON

    # Pro každou kryptoměnu a akcii zavoláme update, pokud data existují
    for crypto in cryptos:
        update_crypto_data(crypto)

    for stock in stocks:
        update_stock_data(stock)

    # Uložíme zaktualizovaná data zpět do JSON
    save_cryptos_to_json(cryptos)
    save_stocks_to_json(stocks)

def display_data():
    cryptos = load_cryptos_from_json()  # Načteme kryptoměny z JSON
    for crypto in cryptos:
        crypto.print_info()

    stocks = load_stocks_from_json()  # Načteme akcie z JSON
    for stock in stocks:
        stock.print_info()

if __name__ == "__main__":
    load_data()  # Načteme a aktualizujeme data
    display_data()  # Vytiskneme informace