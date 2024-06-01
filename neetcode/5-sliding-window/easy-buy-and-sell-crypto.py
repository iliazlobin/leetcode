import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxProfit(self):
        prices = [10, 1, 5, 6, 7, 1]
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, 6)

        prices = [10, 8, 7, 5, 2]
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, 0)

        prices = [1]
        result = self.solution.maxProfit(prices)
        self.assertEqual(result, 0)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices) > 1:
            return 0
        lowest = prices[0]
        res = 0
        for pi, p in enumerate(prices):
            if pi == 0:
                continue
            if p < lowest:
                lowest = p
            else:
                revenue = p - lowest
                res = max(revenue, res)
        return res


if __name__ == "__main__":
    unittest.main()
