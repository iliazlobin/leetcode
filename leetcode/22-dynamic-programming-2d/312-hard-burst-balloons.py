import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxCoins(self):
        self.assertEqual(self.solution.maxCoins([3, 1, 5, 8]), 167, "Example 1 failed")
        self.assertEqual(self.solution.maxCoins([1, 5]), 10, "Example 2 failed")


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            cache[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[i] * nums[l - 1] * nums[r + 1]
                coins += dfs(i + 1, r) + dfs(l, i - 1)
                cache[(l, r)] = max(cache[(l, r)], coins)
            return cache[(l, r)]

        return dfs(1, len(nums) - 2)


if __name__ == "__main__":
    unittest.main()
