import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = Solution()

    def test_insert(self):
        intervals = [[1, 3], [4, 6]]
        newInterval = [2, 5]
        result = self.solution.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 6]])

        intervals = [[1, 2], [3, 5], [9, 10]]
        newInterval = [6, 7]
        result = self.solution.insert(intervals, newInterval)
        self.assertEqual(result, [[1, 2], [3, 5], [6, 7], [9, 10]])


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
                print()
        res.append(newInterval)
        return res


if __name__ == "__main__":
    unittest.main()
