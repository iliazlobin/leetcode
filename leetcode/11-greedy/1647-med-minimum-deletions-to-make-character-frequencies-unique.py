import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minDeletions_example1(self):
        s = "aab"
        expected = 0
        result = self.solution.minDeletions(s)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_minDeletions_example2(self):
        s = "aaabbbcc"
        expected = 2
        result = self.solution.minDeletions(s)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_minDeletions_example3(self):
        s = "ceabaacb"
        expected = 2
        result = self.solution.minDeletions(s)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )

    def test_minDeletions_abcabc(self):
        s = "abcabc"
        expected = 3
        result = self.solution.minDeletions(s)
        self.assertEqual(
            expected, result, f"Failed on input 'abcabc' with {result} != {expected}"
        )

    def test_minDeletions_abcabc(self):
        s = "aab"
        expected = 0
        result = self.solution.minDeletions(s)
        self.assertEqual(
            expected, result, f"Failed on input 'abcabc' with {result} != {expected}"
        )


class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        freqs = set()
        res = 0
        for _, f in count.items():
            while f in freqs and f != 0:
                
                res += 1
                f -= 1
            freqs.add(f)
        return res


if __name__ == "__main__":
    unittest.main()
