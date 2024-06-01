import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minWindow(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(self.solution.minWindow("a", "a"), "a")
        self.assertEqual(self.solution.minWindow("a", "aa"), "")


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                x = s[l]
                window[x] -= 1
                if x in countT and window[x] < countT[x]:
                    have -= 1
                l += 1

        l, r = res
        if l >= 0 and r >= 0:
            return s[l : r + 1]
        else:
            return ""


if __name__ == "__main__":
    unittest.main()
