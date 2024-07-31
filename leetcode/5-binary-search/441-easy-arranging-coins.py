import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_arrangeCoins_example1(self):
        n = 5
        expected_output = 2
        self.assertEqual(self.solution.arrangeCoins(n), expected_output)

    def test_arrangeCoins_example2(self):
        n = 8
        expected_output = 3
        self.assertEqual(self.solution.arrangeCoins(n), expected_output)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            num = (m / 2) * (m + 1)
            if num > n:
                r = m - 1
            else:
                l = m + 1
        return r


class ISolution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        i = 1
        while n >= i:
            n -= i
            res += 1
            i += 1
        return res


if __name__ == "__main__":
    unittest.main()
