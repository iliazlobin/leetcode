import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_minimumLength_example1(self):
    #     s = "ca"
    #     expected_output = 2
    #     self.assertEqual(self.solution.minimumLength(s), expected_output)

    def test_minimumLength_example2(self):
        s = "cabaabac"
        expected_output = 0
        self.assertEqual(self.solution.minimumLength(s), expected_output)

    def test_minimumLength_example3(self):
        s = "aabccabba"
        expected_output = 3
        self.assertEqual(self.solution.minimumLength(s), expected_output)

    def test_minimumLength_largeInput(self):
        s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbacccabbabccaccbacaaccacacccaccbbbacaabbccbbcbcbcacacccccccbcbbabccaacaabacbbaccccbabbcbccccaccacaccbcbbcbcccabaaaabbbbbbbbbbbbbbb"
        expected_output = 109
        self.assertEqual(self.solution.minimumLength(s), expected_output)

    def test_minimumLength_edgeCase(self):
        s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
        expected_output = 1
        self.assertEqual(self.solution.minimumLength(s), expected_output)


class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r and s[l] == s[r]:
            t = s[l]
            while l <= r and s[l] == t:
                l += 1
            while l <= r and s[r] == t:
                r -= 1
        return r - l + 1


class SSolution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r:
            while l > 0 and s[l] == s[l - 1]:
                l += 1
            while r < len(s) - 1 and s[r] == s[r + 1]:
                r -= 1
            if s[l] != s[r]:
                break
            l += 1
            r -= 1
        return r - l + 1 if l < r else 0


if __name__ == "__main__":
    unittest.main()
