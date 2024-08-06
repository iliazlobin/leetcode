from turtle import back
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combinationSum(self):
        result = self.solution.combinationSum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        self.assertEqual(len(result), len(expected))
        self.assertTrue(all(Counter(sub) in map(Counter, expected) for sub in result))

        result = self.solution.combinationSum([2, 3, 5], 8)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(len(result), len(expected))
        self.assertTrue(all(Counter(sub) in map(Counter, expected) for sub in result))

        result = self.solution.combinationSum([2], 1)
        expected = []
        self.assertEqual(result, expected)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # [2, 3, 6, 7], 7
        def dfs(i, total, sub):
            if total == target:
                res.append(sub.copy())
            if i == len(candidates) or total >= target:
                return
            dfs(i, total + candidates[i], sub + [candidates[i]])
            dfs(i + 1, total, sub)

        dfs(0, 0, [])
        return res


class SSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, sub, total):
            if total == target:
                res.append(sub.copy())
                return
            elif total > target:
                return
            if i == len(candidates):
                return
            dfs(i + 1, sub, total)
            dfs(i, sub + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    unittest.main()
