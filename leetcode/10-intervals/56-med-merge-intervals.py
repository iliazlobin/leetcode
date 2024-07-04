import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_intervals(self):
        # Example 1
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), expected)

        # Example 2
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(self.solution.merge(intervals), expected)

        intervals = [[1, 4], [0, 4]]
        expected = [[0, 4]]
        self.assertEqual(self.solution.merge(intervals), expected)

        intervals = [[1, 4], [2, 3]]
        expected = [[1, 4]]
        self.assertEqual(self.solution.merge(intervals), expected)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda k: k[0])

        res = [intervals[0]]
        for i, intv in enumerate(intervals):
            if i == 0:
                continue

            if intv[0] <= res[-1][1]:
                if intv[1] > res[-1][1]:
                    res[-1] = [res[-1][0], intv[1]]
            else:
                res.append(intv)

        return res


if __name__ == "__main__":
    unittest.main()
