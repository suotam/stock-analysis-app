import unittest
from services.api_service import get_crypto_price

class TestApiService(unittest.TestCase):
    def test_get_crypto_price(self):
        price = get_crypto_price("bitcoin")
        self.assertIsNotNone(price)
        self.assertGreater(price, 0)

if __name__ == '__main__':
    unittest.main()