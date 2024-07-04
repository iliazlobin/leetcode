import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxSubArray(self):
        # Example 1
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxSubArray(nums), 6, "Failed for Example 1")

        # Example 2
        nums = [1]
        self.assertEqual(self.solution.maxSubArray(nums), 1, "Failed for Example 2")

        # Example 3
        nums = [5, 4, -1, 7, 8]
        self.assertEqual(self.solution.maxSubArray(nums), 23, "Failed for Example 3")


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = 0
        globalMax = float("-inf")

        for n in nums:
            localMax = max(n, n + localMax)
            globalMax = max(globalMax, localMax)

        return globalMax


class NSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res


if __name__ == "__main__":
    unittest.main()
