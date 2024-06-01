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

        array = []

        def backtrack(i, total):
            if total == target:
                res.append(array.copy())
                return
            elif total > target or i == len(candidates):
                return

            array.append(candidates[i])
            backtrack(i, total + candidates[i])
            array.pop()
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res


if __name__ == "__main__":
    unittest.main()
