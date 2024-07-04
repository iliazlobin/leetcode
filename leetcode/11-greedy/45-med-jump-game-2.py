import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_jump(self):
        nums = [2, 3, 1, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2, "Failed for Example 1")

        nums = [2, 3, 0, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2, "Failed for Example 2")


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        l = r = 0
        jumps = 0
        while r < len(nums) - 1:
            furthest = 0
            jumps += 1
            for i in range(l, r + 1):
                n = nums[i]
                furthest = max(furthest, i + n)
                if i == r:
                    l = r + 1
                    r = furthest

        return jumps


if __name__ == "__main__":
    unittest.main()
