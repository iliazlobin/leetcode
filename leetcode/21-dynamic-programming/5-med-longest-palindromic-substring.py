import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestPalindrome(self):
        # result = self.solution.longestPalindrome("babad")
        # self.assertTrue(result in ["bab", "aba"], "Example 1 failed")

        self.assertEqual(
            self.solution.longestPalindrome("cbbd"), "bb", "Example 2 failed"
        )


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    res = s[l : r + 1]
                    resLen = length
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    res = s[l : r + 1]
                    resLen = length
                l -= 1
                r += 1

        return res


if __name__ == "__main__":
    unittest.main()
