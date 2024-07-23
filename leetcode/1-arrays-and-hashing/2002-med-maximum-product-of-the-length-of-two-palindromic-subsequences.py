import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxProduct_example1(self):
        s = "leetcodecom"
        expected = 9
        result = self.solution.maxProduct(s)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_maxProduct_example2(self):
        s = "bb"
        expected = 1
        result = self.solution.maxProduct(s)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )

    def test_maxProduct_example3(self):
        s = "accbcaxxcxx"
        expected = 25
        result = self.solution.maxProduct(s)
        self.assertEqual(
            expected, result, f"Failed on Example 3 with {result} != {expected}"
        )


class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        palis = {}

        for mask in range(1, 1 << N):
            sub = ""
            for i in range(N):
                if mask & (1 << i):
                    sub += s[N - i - 1]
            if sub == sub[::-1]:
                palis[mask] = len(sub)

        res = 0
        for p1 in palis:
            for p2 in palis:
                if p1 & p2 == 0:
                    res = max(res, palis[p1] * palis[p2])

        return res


if __name__ == "__main__":
    unittest.main()
