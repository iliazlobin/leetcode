import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        # self.solution = SubsetSolution()
        # self.solution = NeetCodeSolution()

    def test_subsetsWithDup(self):
        nums = [1, 2, 1]
        result = self.solution.subsetsWithDup(nums)
        self.assertEqual(
            sorted(result), sorted([[], [1], [1, 2], [1, 1], [1, 2, 1], [2]])
        )

        nums = [7, 7]
        result = self.solution.subsetsWithDup(nums)
        self.assertEqual(sorted(result), sorted([[], [7], [7, 7]]))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                continue
            dfs(i + 1)

        dfs(0)
        return res


class SubsetSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1, subset)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                continue
            dfs(i + 1, subset)

        dfs(0, [])
        return res


class NeetCodeSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


if __name__ == "__main__":
    unittest.main()
