from re import sub
import unittest
from collections import Counter
from typing import List, Optional

from torch import long


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = NeetCodeSolution()

    def test_lengthOfLongestSubstring(self):
        s = "zxyzxyz"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 3)

        s = "xxxx"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 1)

        s = " "
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 1)

        s = "dvdf"
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, 3)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = ""
        current = s[0]
        for ci, c in enumerate(s):
            if ci == 0:
                continue
            duplicate_index = -1
            for vi, v in enumerate(current):
                if c == v:
                    duplicate_index = vi
                    break
            if duplicate_index >= 0:
                if len(current) > len(longest):
                    longest = current
                current = current[duplicate_index + 1 :] + c
                continue
            current += c
        return max(len(longest), len(current))


class NeetCodeSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    unittest.main()
