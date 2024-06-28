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
        total = sum(nums)
        if total % 2:
            return False
        target = total / 2

        dp = set()
        dp.add(0)
        for n in nums:
            clone = dp.copy()
            for e in dp:
                clone.add(e + n)
            dp = clone
        return True if target in dp else False



if __name__ == "__main__":
    unittest.main()
