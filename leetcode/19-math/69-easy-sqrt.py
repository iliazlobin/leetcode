import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_mySqrt(self):
        self.assertEqual(self.solution.mySqrt(4), 2, "The square root of 4 is 2")
        self.assertEqual(
            self.solution.mySqrt(8), 2, "The square root of 8 is rounded down to 2"
        )


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = int((l + r) / 2)
            exp = mid * mid
            if exp > x:
                r = mid - 1
            elif mid < x:
                l = mid + 1
            else:
                return mid
        return r


if __name__ == "__main__":
    unittest.main()
