import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_countSubstrings(self):
        # self.assertEqual(self.solution.countSubstrings("abc"), 3, "Example 1 failed")
        # self.assertEqual(self.solution.countSubstrings("aaa"), 6, "Example 2 failed")
        self.assertEqual(
            self.solution.countSubstrings("fdsklf"), 6, "Failed for input: 'fdsklf'"
        )


class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPali(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        res = 0
        for i in range(len(s)):
            res += countPali(i, i)
            res += countPali(i, i + 1)

        return res


if __name__ == "__main__":
    unittest.main()
