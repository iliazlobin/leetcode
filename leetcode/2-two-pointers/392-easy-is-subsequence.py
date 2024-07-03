import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isSubsequence_example1(self):
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(
            self.solution.isSubsequence(s, t), f"Failed for input: s='{s}', t='{t}'"
        )

    def test_isSubsequence_example2(self):
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(
            self.solution.isSubsequence(s, t), f"Failed for input: s='{s}', t='{t}'"
        )


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == "__main__":
    unittest.main()
