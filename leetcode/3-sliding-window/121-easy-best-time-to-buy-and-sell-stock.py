import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxProfit(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)


class SSolution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j <= i:
                    continue
                profit = max(profit, prices[j] - prices[i])
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            res = max(res, p - lowest)
        return res


if __name__ == "__main__":
    unittest.main()
