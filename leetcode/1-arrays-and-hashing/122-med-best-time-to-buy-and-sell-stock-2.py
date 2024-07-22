import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxProfit_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        result = self.solution.maxProfit(prices)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_maxProfit_example2(self):
        prices = [1, 2, 3, 4, 5]
        expected = 4
        result = self.solution.maxProfit(prices)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_maxProfit_example3(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        result = self.solution.maxProfit(prices)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        profit = 0
        # [7, 1, 5, 3, 6, 4]
        for i in range(1, len(prices)):
            if prev < prices[i]:
                profit += prices[i] - prev
            prev = prices[i]
        return profit


if __name__ == "__main__":
    unittest.main()
