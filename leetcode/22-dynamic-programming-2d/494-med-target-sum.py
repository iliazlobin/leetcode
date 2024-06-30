import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findTargetSumWays(self):
        # self.assertEqual(
        #     self.solution.findTargetSumWays([1, 1], 2), 1, "Example 1 failed"
        # )
        self.assertEqual(
            self.solution.findTargetSumWays([1, 1, 1, 1, 1], 3), 5, "Example 1 failed"
        )
        self.assertEqual(self.solution.findTargetSumWays([1], 1), 1, "Example 2 failed")


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]

            r = dfs(i + 1, total - nums[i]) + dfs(i + 1, total + nums[i])
            cache[(i, total)] = r
            return r

        return dfs(0, 0)


if __name__ == "__main__":
    unittest.main()
