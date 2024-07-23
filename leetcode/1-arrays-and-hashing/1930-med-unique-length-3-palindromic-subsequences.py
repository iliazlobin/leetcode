import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countPalindromicSubsequence_example1(self):
        s = "aabca"
        expected = 3
        result = self.solution.countPalindromicSubsequence(s)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_countPalindromicSubsequence_example2(self):
        s = "adc"
        expected = 0
        result = self.solution.countPalindromicSubsequence(s)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_countPalindromicSubsequence_example3(self):
        s = "bbcbaba"
        expected = 4
        result = self.solution.countPalindromicSubsequence(s)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = defaultdict(int)
        for i, c in enumerate(s):
            if i > 0:
                right[c] += 1
        res = set()  # key=(mid, out)
        left = set(s[0])
        for i in range(1, len(s) - 1):
            m = s[i]
            right[m] -= 1
            for o in range(ord("a"), ord("z") + 1):
                c = chr(o)
                if c in left and right[c] > 0:
                    res.add((m, c))
            left.add(m)
        return len(res)


if __name__ == "__main__":
    unittest.main()
