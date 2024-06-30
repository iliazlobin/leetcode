import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isMatch(self):
        self.assertFalse(self.solution.isMatch("aa", "a"), "Example 1 failed")
        self.assertTrue(self.solution.isMatch("aa", "a*"), "Example 2 failed")
        self.assertTrue(self.solution.isMatch("ab", ".*"), "Example 3 failed")
        self.assertTrue(
            self.solution.isMatch("aab", "c*a*b"),
            "Test with s='aab' and p='c*a*b' failed",
        )
        self.assertTrue(
            self.solution.isMatch("nnn", "n*"), "Test with s='nnn' and p='n*' failed"
        )
        self.assertFalse(
            self.solution.isMatch("aa", ".b"), "Test with s='aa' and p='.b' failed"
        )


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            cache[(i, j)] = False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j < len(p) - 1 and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            if not cache[(i, j)] and match:
                cache[(i, j)] = dfs(i + 1, j + 1)

            return cache[(i, j)]

        return dfs(0, 0)


if __name__ == "__main__":
    unittest.main()
