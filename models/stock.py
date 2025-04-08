class Stock:
    def __init__(self, name, price, volume):
        self.name = name
        self.price = price
        self.volume = volume
    
    def print_info(self):
        print(f"Stock: {self.name}, Price: {self.price}, Volume: {self.volume}")