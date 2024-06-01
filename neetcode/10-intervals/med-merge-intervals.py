import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = NeetCodeSolution()

    def test_merge(self):
        intervals = [[1, 3], [1, 5], [6, 7]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 5], [6, 7]])

        intervals = [[1, 2], [2, 3]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 3]])

        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[1, 6], [8, 10], [15, 18]])

        intervals = [[1, 4], [0, 4]]
        result = self.solution.merge(intervals)
        self.assertEqual(result, [[0, 4]])


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        res = []
        new = intervals[0]
        for i, inv in enumerate(intervals):
            if i == 0:
                continue
            if new[1] < inv[0]:
                res.append(new)
                if len(intervals) - 1 == i:
                    res.append(inv)
                    return res
                new = intervals[i]
                continue
            new: List[int] = [new[0], max(new[1], inv[1])]
        res.append(new)
        return res


class NeetCodeSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


if __name__ == "__main__":
    unittest.main()
