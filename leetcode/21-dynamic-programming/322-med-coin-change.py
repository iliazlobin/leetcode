import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_coinChange(self):
        # self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3, "Example 1 failed")
        self.assertEqual(self.solution.coinChange([2], 3), -1, "Example 2 failed")
        # self.assertEqual(self.solution.coinChange([1], 0), 0, "Example 3 failed")


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    unittest.main()
