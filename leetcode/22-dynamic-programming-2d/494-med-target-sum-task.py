import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findTargetSumWays(self):
        self.assertEqual(
            self.solution.findTargetSumWays([1, 1], 2), 1, "Example 1 failed"
        )
        self.assertEqual(
            self.solution.findTargetSumWays([1, 1, 1, 1, 1], 3), 5, "Example 1 failed"
        )
        self.assertEqual(self.solution.findTargetSumWays([1], 1), 1, "Example 2 failed")
        self.assertEqual(
            self.solution.findTargetSumWays([2, 2, 2], 2),
            3,
            "Additional example failed",
        )


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return None


if __name__ == "__main__":
    unittest.main()
