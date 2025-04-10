from models.crypto import Crypto
from services.crypto_service import update_crypto_data, save_cryptos_to_json, load_cryptos_from_json, add_new_crypto, remove_crypto_from_json, update_all_cryptos, update_crypto
from services.stock_service import update_stock_data, save_stocks_to_json, load_stocks_from_json, add_new_stock, remove_stock_from_json, update_all_stocks, update_stock

def load_data():
    cryptos = load_cryptos_from_json()  
    stocks = load_stocks_from_json()   

    for crypto in cryptos:
        update_crypto(crypto)

    for stock in stocks:
        update_stock(stock)

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

def update_all_investments():
    update_all_cryptos()  # Aktualizuje všechny kryptoměny
    update_all_stocks()   # Aktualizuje všechny akcie

def remove_investment():
    investment_type = input("Chcete odstranit kryptoměnu nebo akcii? (crypto/stock): ").strip().lower()
    if investment_type == 'crypto':
        crypto_name = input("Zadejte název kryptoměny, kterou chcete odstranit: ").strip()
        remove_crypto_from_json(crypto_name)
    elif investment_type == 'stock':
        stock_name = input("Zadejte symbol akcie, kterou chcete odstranit: ").strip()
        remove_stock_from_json(stock_name)
    else:
        print("Neplatná volba! Zkuste to znovu.")

def test_environment():
    while True:
        print("\n--- Testovací prostředí ---")
        print("1. Přidat novou kryptoměnu")
        print("2. Přidat novou akcii")
        print("3. Aktualizovat všechny kryptoměny")
        print("4. Aktualizovat všechny akcie")
        print("5. Zobrazit data o kryptoměnách a akciích")
        print("6. Odstranit kryptoměnu nebo akcii")
        print("7. Ukončit")

        choice = input("Vyberte číslo akce (1-7): ").strip()

        if choice == '1':
            add_new_investment()
        elif choice == '2':
            add_new_investment()
        elif choice == '3':
            update_all_investments()
        elif choice == '4':
            update_all_investments()
        elif choice == '5':
            display_data()
        elif choice == '6':
            remove_investment()
        elif choice == '7':
            print("Ukončuji aplikaci...")
            break
        else:
            print("Neplatná volba! Zkuste to znovu.")

if __name__ == "__main__":
    load_data()  
    test_environment()