import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canPartition(self):
        self.assertTrue(self.solution.canPartition([1, 5, 11, 5]), "Example 1 failed")
        self.assertFalse(self.solution.canPartition([1, 2, 3, 5]), "Example 2 failed")
        nums = [2, 2, 1, 1]
        expected = True
        self.assertEqual(
            self.solution.canPartition(nums), expected, f"Failed for input: {nums}"
        )


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return None


if __name__ == "__main__":
    unittest.main()
