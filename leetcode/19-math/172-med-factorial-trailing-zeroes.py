import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_trailingZeroes(self):
        self.assertEqual(self.solution.trailingZeroes(3), 0, "3! has no trailing zero")
        self.assertEqual(self.solution.trailingZeroes(5), 1, "5! has one trailing zero")
        self.assertEqual(self.solution.trailingZeroes(0), 0, "0! has no trailing zero")


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n /= 5
            res += int(n)
        return res


if __name__ == "__main__":
    unittest.main()
