import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_myPow(self):
        self.assertAlmostEqual(
            self.solution.myPow(2.00000, 10),
            1024.00000,
            places=5,
            msg="2^10 should be 1024",
        )
        self.assertAlmostEqual(
            self.solution.myPow(2.10000, 3),
            9.26100,
            places=5,
            msg="2.1^3 should be approximately 9.261",
        )
        self.assertAlmostEqual(
            self.solution.myPow(2.00000, -2),
            0.25000,
            places=5,
            msg="2^-2 should be 0.25",
        )


class XSolution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        N = abs(n)
        res = x
        elems = 1
        while N - elems >= elems:
            res *= res
            elems *= 2
        # need to account for smaller batches, can use cache for instance
        for i in range(N - elems):
            res *= x
        return res if n >= 0 else 1 / res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res


if __name__ == "__main__":
    unittest.main()
