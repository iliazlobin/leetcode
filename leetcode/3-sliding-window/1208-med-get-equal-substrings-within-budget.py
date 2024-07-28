import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_equalSubstring_example1(self):
        s = "abcd"
        t = "bcdf"
        maxCost = 3
        expected_output = 3
        self.assertEqual(self.solution.equalSubstring(s, t, maxCost), expected_output)

    def test_equalSubstring_example2(self):
        s = "abcd"
        t = "cdef"
        maxCost = 3
        expected_output = 1
        self.assertEqual(self.solution.equalSubstring(s, t, maxCost), expected_output)

    def test_equalSubstring_example3(self):
        s = "abcd"
        t = "acde"
        maxCost = 0
        expected_output = 1
        self.assertEqual(self.solution.equalSubstring(s, t, maxCost), expected_output)


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [0] * len(s)
        for i in range(len(s)):
            c = abs(ord(s[i]) - ord(t[i]))
            cost[i] = c
        l = 0
        total = 0
        res = 0
        for r in range(len(s)):
            total += cost[r]
            if total > maxCost:
                total -= cost[l]
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    unittest.main()
