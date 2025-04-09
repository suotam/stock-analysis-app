class Crypto:
    def __init__(self, name, price=None, currency="USD"):
        self.name = name
        self.price = price
        self.currency = currency

    def print_info(self):
        print(f"Kryptoměna: {self.name}, Cena: {self.price} {self.currency}")