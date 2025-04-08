from datetime import datetime

class StockSnapshot:
    def __init__(self, stock, price, timestamp=None):
        self.stock = stock
        self.price = price
        self.timestamp = timestamp or datetime.now()
    
    def print_snapshot(self):
        print(f"Stock: {self.stock.name}, Price: {self.price}, Timestamp: {self.timestamp}")