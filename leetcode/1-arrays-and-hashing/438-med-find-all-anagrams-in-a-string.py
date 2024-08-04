import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findAnagrams_example1(self):
        s = "cbaebabacd"
        p = "abc"
        expected_output = [0, 6]
        self.assertEqual(self.solution.findAnagrams(s, p), expected_output)

    def test_findAnagrams_example2(self):
        s = "abab"
        p = "ab"
        expected_output = [0, 1, 2]
        self.assertEqual(self.solution.findAnagrams(s, p), expected_output)


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pChars = [0] * 26
        for c in p:
            n = ord(c) - ord("a")
            pChars[n] += 1

        sChars = [0] * 26
        l = 0
        res = []
        for r in range(len(s)):
            n = ord(s[r]) - ord("a")
            sChars[n] += 1
            if r >= len(p) - 1:
                if tuple(pChars) == tuple(sChars):
                    res.append(l)
                c = n = ord(s[l]) - ord("a")
                sChars[c] -= 1
                l += 1
        return res


if __name__ == "__main__":
    unittest.main()
