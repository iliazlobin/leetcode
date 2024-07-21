import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_StockSpanner(self):
        stockSpanner = StockSpanner()
        self.assertEqual(stockSpanner.next(100), 1)
        self.assertEqual(stockSpanner.next(80), 1)
        self.assertEqual(stockSpanner.next(60), 1)
        self.assertEqual(stockSpanner.next(70), 2)
        self.assertEqual(stockSpanner.next(60), 1)
        self.assertEqual(stockSpanner.next(75), 4)
        self.assertEqual(stockSpanner.next(85), 6)


class StockSpanner:
    stock = []

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        i = len(self.stock) - 1
        span = 1
        while i >= 0 and self.stock[i][0] <= price:
            span += self.stock[i][1]
            i -= self.stock[i][1]
        self.stock.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == "__main__":
    unittest.main()
