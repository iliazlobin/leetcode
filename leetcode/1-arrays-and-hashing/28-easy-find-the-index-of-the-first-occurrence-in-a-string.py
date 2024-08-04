import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_strStr_example1(self):
        haystack = "sadbutsad"
        needle = "sad"
        expected_output = 0
        self.assertEqual(self.solution.strStr(haystack, needle), expected_output)

    def test_strStr_example2(self):
        haystack = "leetcode"
        needle = "leeto"
        expected_output = -1
        self.assertEqual(self.solution.strStr(haystack, needle), expected_output)

    def test_strStr_example3(self):
        haystack = "mississippi"
        needle = "issip"
        expected_output = 4
        self.assertEqual(self.solution.strStr(haystack, needle), expected_output)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = 0, 0
        while h <= len(haystack) - len(needle):
            if haystack[h : h + len(needle)] == needle:
                return h
            h += 1
        return -1


class SSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = 0, 0
        while h < len(haystack) and n < len(needle):
            if haystack[h] == needle[n]:
                n += 1
            else:
                h -= n
                n = 0
            h += 1
        return h - len(needle) if n == len(needle) else -1


if __name__ == "__main__":
    unittest.main()
