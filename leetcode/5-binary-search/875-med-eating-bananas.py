import math
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minEatingSpeed(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 4)

        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 30)

        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(self.solution.minEatingSpeed(piles, h), 23)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

if __name__ == "__main__":
    unittest.main()
