import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4, "Example 1 failed")
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12, "Example 2 failed")

        nums = [2, 1, 1, 2]
        expected = 4
        self.assertEqual(self.solution.rob(nums), expected, f"Failed for input: {nums}")


class Solution:
    def rob(self, nums: List[int]) -> int:
        return None


if __name__ == "__main__":
    unittest.main()
