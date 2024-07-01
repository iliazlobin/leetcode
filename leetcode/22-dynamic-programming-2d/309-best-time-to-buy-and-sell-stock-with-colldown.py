import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxProfit(self):
        self.assertEqual(
            self.solution.maxProfit([1, 2, 3, 0, 2]), 3, "Example 1 failed"
        )
        self.assertEqual(self.solution.maxProfit([1]), 0, "Example 2 failed")


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]
            cooldown = dfs(i + 1, buying)
            if buying:
                operation = dfs(i + 1, False) - prices[i]
            else:
                operation = dfs(i + 2, True) + prices[i]
            maxi = max(cooldown, operation)
            cache[(i, buying)] = maxi
            return maxi

        return dfs(0, True)


class PSolution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, buying):
            if (i, buying) in cache:
                return cache[(i, buying)]
            if i >= len(prices):
                return 0

            cache[(i, buying)] = 0
            if buying:
                cache[(i, buying)] = max(
                    dfs(i + 1, False) - prices[i], dfs(i + 1, True)
                )
            else:
                cache[(i, buying)] = max(
                    dfs(i + 2, True) + prices[i], dfs(i + 1, False)
                )

            return cache[(i, buying)]

        return dfs(0, True)


if __name__ == "__main__":
    unittest.main()
