import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_getSum(self):
        a, b = 1, 2
        self.assertEqual(self.solution.getSum(a, b), 3)

        a, b = 2, 3
        self.assertEqual(self.solution.getSum(a, b), 5)

        a, b = -1, 1
        self.assertEqual(self.solution.getSum(a, b), 0)

        a, b = -12, -8
        self.assertEqual(self.solution.getSum(a, b), -20)


class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            tmp = ((a & b) << 1) & 0xFFFFFFFF
            a = (a ^ b) & 0xFFFFFFFF
            b = tmp
        if a > 0x7FFFFFFF:
            a = ~(a ^ 0xFFFFFFFF)
        return a


if __name__ == "__main__":
    unittest.main()
