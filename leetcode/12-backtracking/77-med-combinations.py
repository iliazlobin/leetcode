import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combine_example1(self):
        n = 4
        k = 2
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        result = self.solution.combine(n, k)
        self.assertEqual(
            len(expected),
            len(result),
            f"Expected and result lengths differ: {len(expected)} != {len(result)}",
        )
        for combo in expected:
            self.assertIn(combo, result, f"Combo {combo} not in result")

    def test_combine_example2(self):
        n = 1
        k = 1
        expected = [[1]]
        result = self.solution.combine(n, k)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
            if i > n:
                return

            dfs(i + 1, sub)
            dfs(i + 1, sub + [i])

        dfs(1, [])
        return res


if __name__ == "__main__":
    unittest.main()
