import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minWindow(self):
        # self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        # self.assertEqual(self.solution.minWindow("a", "a"), "a")
        self.assertEqual(self.solution.minWindow("a", "aa"), "")


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        total = 0
        tCount = {}
        for c in t:
            if c in tCount:
                tCount[c] += 1
            else:
                tCount[c] = 1
                total += 1

        sCount = {}
        l = r = 0
        shortest = float("inf")
        sl, sr = 0, 0
        matches = 0
        while r < len(s):
            if s[r] in tCount:
                sCount[s[r]] = sCount.get(s[r], 0) + 1
                if sCount[s[r]] == tCount[s[r]]:
                    matches += 1

            while matches == total:

                if s[l] in sCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] + 1 == tCount[s[l]]:
                        matches -= 1

                        length = r - l + 1
                        if length < shortest:
                            shortest = length
                            sl = l
                            sr = r
                l += 1

            r += 1

        return s[sl:sr+1] if shortest != float("inf") else ""


if __name__ == "__main__":
    unittest.main()
