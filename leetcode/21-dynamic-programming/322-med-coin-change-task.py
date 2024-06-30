import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_coinChange(self):
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3, "Example 1 failed")
        self.assertEqual(self.solution.coinChange([2], 3), -1, "Example 2 failed")
        self.assertEqual(self.solution.coinChange([1], 0), 0, "Example 3 failed")


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return None


if __name__ == "__main__":
    unittest.main()
