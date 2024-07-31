import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPerfectSquare_example1(self):
        num = 16
        expected_output = True
        self.assertEqual(self.solution.isPerfectSquare(num), expected_output)

    def test_isPerfectSquare_example2(self):
        num = 14
        expected_output = False
        self.assertEqual(self.solution.isPerfectSquare(num), expected_output)


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            square = m * m
            if square > num:
                r = m - 1
            elif square < num:
                l = m + 1
            else:
                return True
        return False



if __name__ == "__main__":
    unittest.main()
