from turtle import back
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combinationSum2(self):
        # result = self.solution.combinationSum2([1, 1, 2, 5, 6, 7, 10], 8)
        result = self.solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertEqual(len(result), len(expected))
        self.assertTrue(all(Counter(sub) in map(Counter, expected) for sub in result))

        result = self.solution.combinationSum2([2, 5, 2, 1, 2], 5)
        expected = [[1, 2, 2], [5]]
        self.assertEqual(len(result), len(expected))
        self.assertTrue(all(Counter(sub) in map(Counter, expected) for sub in result))


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1:
            if candidates[0] == target:
                return [[candidates[0]]]
            else:
                return [[]]
        res = []
        candidates.sort()

        def backtrack(i, total, array):
            if total == target:
                res.append(array.copy())
                return
            if i == len(candidates) - 1:
                return

            prev = -1
            for i in range(i, len(candidates)):
                if candidates[i] == prev:
                    continue
                array.append(candidates[i])
                backtrack(i + 1, total + candidates[i], array)
                array.pop()
                prev = candidates[i]

        backtrack(0, 0, [])
        return res


class NSolution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res


if __name__ == "__main__":
    unittest.main()
