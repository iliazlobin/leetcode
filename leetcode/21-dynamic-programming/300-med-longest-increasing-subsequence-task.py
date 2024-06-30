import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLIS(self):
        self.assertEqual(
            self.solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]),
            4,
            "Example 1 failed",
        )

        self.assertEqual(
            self.solution.lengthOfLIS([0, 1, 0, 3, 2, 3]), 4, "Example 2 failed"
        )

        self.assertEqual(
            self.solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1, "Example 3 failed"
        )


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return None


if __name__ == "__main__":
    unittest.main()
