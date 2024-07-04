import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canJump(self):
        nums = [2, 3, 1, 1, 4]
        self.assertTrue(self.solution.canJump(nums), "Failed for Example 1")

        nums = [3, 2, 1, 0, 4]
        self.assertFalse(self.solution.canJump(nums), "Failed for Example 2")

        nums = [0, 1]
        self.assertFalse(self.solution.canJump(nums), "Failed with initial zero")

        nums = [2, 0]
        self.assertTrue(self.solution.canJump(nums), "Failed with small positive start")

        nums = [2, 0, 0]
        self.assertTrue(self.solution.canJump(nums), "Failed with consecutive zeros")


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        r = len(nums) - 1
        l = r - 1
        while l >= 0:
            if nums[l] >= r - l:
                r = l
                l = r - 1
            else:
                l -= 1
        return r == 0


if __name__ == "__main__":
    unittest.main()
