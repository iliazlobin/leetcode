import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_characterReplacement(self):
        self.assertEqual(self.solution.characterReplacement("XYYX", 2), 4)
        self.assertEqual(self.solution.characterReplacement("AAABABB", 1), 5)
        self.assertEqual(self.solution.characterReplacement("AABABBA", 1), 4)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            if r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1


if __name__ == "__main__":
    unittest.main()
