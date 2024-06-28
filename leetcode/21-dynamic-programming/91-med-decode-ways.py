import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_decodeWays(self):
        self.assertEqual(self.solution.numDecodings("12"), 2, "Example 1 failed")
        self.assertEqual(self.solution.decodeWays("01"), 0, "Example 2 failed")


class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}

        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
            ):
                res += dfs(i + 2)
            cache[i] = res
            return res

        return dfs(0)


if __name__ == "__main__":
    unittest.main()
