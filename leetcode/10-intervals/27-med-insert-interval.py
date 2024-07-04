import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_insert_interval(self):
        # # Example 1
        # intervals = [[1, 3], [6, 9]]
        # newInterval = [2, 5]
        # expected = [[1, 5], [6, 9]]
        # self.assertEqual(self.solution.insert(intervals, newInterval), expected)

        # # Example 2
        # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        # newInterval = [4, 8]
        # expected = [[1, 2], [3, 10], [12, 16]]
        # self.assertEqual(self.solution.insert(intervals, newInterval), expected)

        # intervals = []
        # newInterval = [5, 7]
        # expected = [[5, 7]]
        # self.assertEqual(self.solution.insert(intervals, newInterval), expected)

        intervals = [[1, 5]]
        newInterval = [2, 7]
        expected = [[1, 7]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)


# Ot(n), Om(n)
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
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        return res if len(res) > 0 else [newInterval]

class FSolution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        inserted = False
        if newInterval[0] < intervals[0][0]:
            res = [newInterval]
            inserted = True
        else:
            res = [intervals[0]]

        for i, intv in enumerate(intervals):
            if i == 0 and not inserted:
                continue

            if newInterval[0] <= intv[0]:
                if newInterval[0] <= res[-1][1]:
                    if newInterval[1] >= res[-1][1]:
                        res[-1] = [res[-1][0], newInterval[1]]
                else:
                    res.append(newInterval)
                inserted = True

            if intv[0] <= res[-1][1]:
                if intv[1] >= res[-1][1]:
                    res[-1] = [res[-1][0], intv[1]]
            else:
                res.append(intv)

        if not inserted:
            if newInterval[0] <= res[-1][1]:
                if newInterval[1] >= res[-1][1]:
                    res[-1] = [res[-1][0], newInterval[1]]
            else:
                res.append(newInterval)

        return res


if __name__ == "__main__":
    unittest.main()
