import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numDistinct(self):
        self.assertEqual(
            self.solution.numDistinct("caaat", "cat"), 3, "Example 1 failed"
        )
        self.assertEqual(
            self.solution.numDistinct("xxyxy", "xy"), 5, "Example 2 failed"
        )


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            if i == len(s):
                return 1 if j == len(t) else 0
            if j == len(t):
                return 1

            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            res += dfs(i + 1, j)

            return res

        return dfs(0, 0)


if __name__ == "__main__":
    unittest.main()
