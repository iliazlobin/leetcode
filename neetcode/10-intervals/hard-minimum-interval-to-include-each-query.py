from math import inf
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minInterval(self):
        intervals = [[1, 3], [2, 3], [3, 7], [6, 6]]
        queries = [2, 3, 1, 7, 6, 8]
        result = self.solution.minInterval(intervals, queries)
        self.assertEqual(result, [2, 2, 3, 5, 1, -1])

        intervals = [[2,3],[2,5],[1,8],[20,25]]
        queries = [2,19,5,22]
        result = self.solution.minInterval(intervals, queries)
        self.assertEqual(result, [2,-1,4,6])


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        b = 0
        output = []
        for q in queries:
            min_l = float("inf")
            for i in intervals[b:]:
                if q >= i[0] and q <= i[1]:
                    l = i[1] - i[0] + 1
                    min_l = min(min_l, l)
                    print()
            if min_l == float("inf"):
                min_l = -1
            output.append(min_l)
        return output


if __name__ == "__main__":
    unittest.main()
