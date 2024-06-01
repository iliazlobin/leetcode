import heapq
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = Solution()

    def test_lastStoneWeight(self):
        stones = [2, 3, 6, 2, 4]
        result = self.solution.lastStoneWeight(stones)
        self.assertEqual(result, 1)

        stones = [1, 2]
        result = self.solution.lastStoneWeight(stones)
        self.assertEqual(result, 1)


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nstones = [-s for s in stones]
        heapq.heapify(nstones)
        while len(nstones) > 1:
            first = heapq.heappop(nstones)
            second = heapq.heappop(nstones)
            sum = first - second
            if sum != 0:
                heapq.heappush(nstones, sum)
        if len(nstones) == 0:
            return 0
        return abs(nstones[0])


if __name__ == "__main__":
    unittest.main()
