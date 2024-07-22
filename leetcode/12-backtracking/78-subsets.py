from turtle import back
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsets(self):
        result = self.solution.subsets([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        self.assertEqual(len(result), len(expected))
        self.assertTrue(all(Counter(sub) in map(Counter, expected) for sub in result))

        result = self.solution.subsets([0])
        expected = [[], [0]]
        self.assertEqual(len(result), len(expected))
        self.assertTrue(all(Counter(sub) in map(Counter, expected) for sub in result))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, sub):
            if i == len(nums):
                res.append(sub.copy())
                return

            dfs(i + 1, sub)
            dfs(i + 1, sub + [nums[i]])

        dfs(0, [])
        return res


class XSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res


if __name__ == "__main__":
    unittest.main()
