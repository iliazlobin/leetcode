import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition(self):
        # s = "aab"
        # result = self.solution.partition(s)
        # self.assertEqual(sorted(result), sorted([["a", "a", "b"], ["aa", "b"]]))

        # s = "a"
        # result = self.solution.partition(s)
        # self.assertEqual(sorted(result), sorted([["a"]]))

        s = "abbab"
        result = self.solution.partition(s)
        self.assertEqual(
            sorted(result),
            sorted(
                [
                    ["a", "b", "b", "a", "b"],
                    ["a", "b", "bab"],
                    ["a", "bb", "a", "b"],
                    ["abba", "b"],
                ]
            ),
        )


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        sLen = len(s)

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    unittest.main()
