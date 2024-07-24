import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "abc"
        t = "ahbgdc"
        self.assertTrue(self.solution.isSubsequence(s, t))

    def test_example2(self):
        s = "axc"
        t = "ahbgdc"
        self.assertFalse(self.solution.isSubsequence(s, t))

    def test_empty_s(self):
        s = ""
        t = "ahbgdc"
        self.assertTrue(self.solution.isSubsequence(s, t))

    def test_empty_t(self):
        s = "abc"
        t = ""
        self.assertFalse(self.solution.isSubsequence(s, t))

    def test_both_empty(self):
        s = ""
        t = ""
        self.assertTrue(self.solution.isSubsequence(s, t))


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


class HSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        chars = {}
        total = 0
        for c in s:
            chars[c] = chars.get(c, 0) + 1
            total += 1
        for c in t:
            if c in chars and chars[c] > 0:
                chars[c] -= 1
                total -= 1
                if total == 0:
                    return True
        return False


if __name__ == "__main__":
    unittest.main()
