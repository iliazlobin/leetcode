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
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(0, len(nums) - 2, 1):
            nums[i + 2] = max(nums[i] + nums[i + 2], nums[i + 1])
        return max(nums[-2], nums[-1])


class NSolution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

if __name__ == "__main__":
    unittest.main()
