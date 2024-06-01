import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = NeetCodeSolution()

    def test_minEatingSpeed(self):
        piles: List[int] = [3, 6, 7, 11]
        h = 8
        result = self.solution.minEatingSpeed(piles, h)
        self.assertEqual(result, 4)

        piles = [1, 4, 3, 2]
        h = 9
        result = self.solution.minEatingSpeed(piles, h)
        self.assertEqual(result, 2)

        piles = [25, 10, 23, 4]
        h = 4
        result = self.solution.minEatingSpeed(piles, h)
        self.assertEqual(result, 25)

        # requies efficient searhc (from both sides)
        piles = [312884470]
        h = 312884469
        result = self.solution.minEatingSpeed(piles, h)
        self.assertEqual(result, 2)


import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sorted_piles = sorted(piles, reverse=True)
        prev_k = None
        ind = 0
        cur_k = sorted_piles[ind]
        while True:
            cur_h = 0
            for pi, p in enumerate(sorted_piles):
                cur_h += math.ceil(float(p) / cur_k)
            print(cur_k, cur_h, h)
            if cur_h > h:
                if prev_k is None:
                    raise Exception("Impossible to solve")
                return prev_k
            prev_k = cur_k
            cur_k -= 1
            if cur_k == 0:
                raise Exception("Speed can't be 0")


class NeetCodeSolution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


if __name__ == "__main__":
    unittest.main()
