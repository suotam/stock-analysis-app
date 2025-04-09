class Stock:
    def __init__(self, name, price=None, volume=None):
        self.name = name
        self.price = price
        self.volume = volume

    def print_info(self):
        print(f"Akcie: {self.name}, Cena: {self.price}, Objem: {self.volume}")