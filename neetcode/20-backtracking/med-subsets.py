import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsets(self):
        nums = [1, 2, 3]
        result = self.solution.subsets(nums)
        self.assertEqual(
            sorted(result),
            sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        )

        nums = [7]
        result = self.solution.subsets(nums)
        self.assertEqual(sorted(result), sorted([[], [7]]))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


if __name__ == "__main__":
    unittest.main()
