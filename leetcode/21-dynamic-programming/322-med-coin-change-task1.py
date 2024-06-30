import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_coinChange(self):
        # self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3, "Example 1 failed")
        # self.assertEqual(self.solution.coinChange([2], 3), -1, "Example 2 failed")
        # self.assertEqual(self.solution.coinChange([1], 0), 0, "Example 3 failed")

        coins = [1, 2, 5]
        amount = 11
        expected = 3
        self.assertEqual(
            self.solution.coinChange(coins, amount),
            expected,
            f"Failed for coins={coins} and amount={amount}",
        )


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float("inf")
        cache = {}
        for i in range(amount - 1, -1, -1):
            fewest = MAX
            for c in coins:
                if amount - i == c:
                    cache[i] = 1
                    break
                elif i + c in cache:
                    fewest = min(fewest, cache[i + c] + 1)
            if i not in cache:
                cache[i] = fewest

        if amount == 0:
            return 0
        return cache[0] if len(cache) > 0 and cache[0] != MAX else -1


if __name__ == "__main__":
    unittest.main()
