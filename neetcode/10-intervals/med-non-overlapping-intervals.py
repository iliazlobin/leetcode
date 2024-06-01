import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_eraseOverlapIntervals(self):
        intervals = [[1,2],[2,4],[1,4]]
        result = self.solution.eraseOverlapIntervals(intervals)
        self.assertEqual(result, 1)

        intervals = [[1,2],[2,4]]
        result = self.solution.eraseOverlapIntervals(intervals)
        self.assertEqual(result, 0)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        prev_end = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
                prev_end = min(prev_end, end)
        return res


if __name__ == "__main__":
    unittest.main()
