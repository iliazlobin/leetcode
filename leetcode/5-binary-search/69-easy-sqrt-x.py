import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mySqrt_example1(self):
        x = 4
        expected_output = 2
        self.assertEqual(self.solution.mySqrt(x), expected_output)

    def test_mySqrt_example2(self):
        x = 8
        expected_output = 2
        self.assertEqual(self.solution.mySqrt(x), expected_output)


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            exp = m * m
            if exp > x:
                r = m - 1
            else:
                l = m + 1
        return r


if __name__ == "__main__":
    unittest.main()
