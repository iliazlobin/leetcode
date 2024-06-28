import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob(self):
        self.assertEqual(self.solution.rob([2, 3, 2]), 3, "Example 1 failed")

        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4, "Example 2 failed")

        self.assertEqual(self.solution.rob([1, 2, 3]), 3, "Example 3 failed")


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = temp

        return rob2


if __name__ == "__main__":
    unittest.main()
