from models.crypto import Crypto
from services.crypto_service import update_crypto_data, save_cryptos_to_json, load_cryptos_from_json, add_new_crypto, remove_crypto_from_json
from services.stock_service import update_stock_data, save_stocks_to_json, load_stocks_from_json, add_new_stock, remove_stock_from_json

def load_data():
    cryptos = load_cryptos_from_json()  
    stocks = load_stocks_from_json()   

    for crypto in cryptos:
        update_crypto_data(crypto)

    for stock in stocks:
        update_stock_data(stock)

    save_cryptos_to_json(cryptos)
    save_stocks_to_json(stocks)

def display_data():
    cryptos = load_cryptos_from_json()  
    for crypto in cryptos:
        crypto.print_info()

    stocks = load_stocks_from_json()  
    for stock in stocks:
        stock.print_info()

def add_new_investment():
    crypto_name = input("Zadejte název kryptoměny (např. 'DOGE'): ")
    add_new_crypto(crypto_name)

    stock_name = input("Zadejte symbol akcie (např. 'MSFTDO'): ")
    add_new_stock(stock_name)


if __name__ == "__main__":
    load_data()  
    remove_stock_from_json('fds')
    remove_crypto_from_json('dogecoin')
    display_data()  