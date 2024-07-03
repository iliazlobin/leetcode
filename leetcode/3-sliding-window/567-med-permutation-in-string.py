import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_checkInclusion(self):
        self.assertTrue(self.solution.checkInclusion("ab", "eidbaooo"))
        self.assertFalse(self.solution.checkInclusion("ab", "eidboaoo"))
        self.assertFalse(self.solution.checkInclusion("hello", "ooolleoooleh"))
        self.assertTrue(self.solution.checkInclusion("abc", "bbbca"))

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        uniques = 0
        for c in s1:
            if c in s1Count:
                s1Count[c] += 1
            else:
                s1Count[c] = 1
                uniques += 1

        s2Count = {}
        matches = 0
        for i, c in enumerate(s2):
            if c in s1Count:
                s2Count[c] = s2Count.get(c, 0) + 1

                if s1Count[c] == s2Count[c]:
                    matches += 1
                elif s1Count[c] + 1 == s2Count[c]:
                    matches -= 1

            if i >= len(s1):
                p = s2[i - len(s1)]
                if p in s2Count:
                    s2Count[p] -= 1

                    if s1Count[p] == s2Count[p]:
                        matches += 1
                    elif s1Count[p] - 1 == s2Count[p]:
                        matches -= 1

            if matches == uniques:
                return True

        return False


class NSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1

        return matches == 26


if __name__ == "__main__":
    unittest.main()
