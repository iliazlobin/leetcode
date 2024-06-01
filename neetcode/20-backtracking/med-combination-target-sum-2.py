from ast import Num
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combinationSum2(self):
        candidates = [9, 2, 2, 4, 6, 1, 5]
        target = 8
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(sorted(result), sorted([[1, 2, 5], [2, 2, 4], [2, 6]]))

        candidates = [1, 2, 3, 4, 5]
        target = 7
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(sorted(result), sorted([[1, 2, 4], [2, 5], [3, 4]]))


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur: list, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            cur.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


if __name__ == "__main__":
    unittest.main()
