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
        return None

if __name__ == "__main__":
    unittest.main()
