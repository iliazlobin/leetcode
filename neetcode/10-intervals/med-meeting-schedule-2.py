import unittest
from collections import Counter
from typing import List, Optional


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minMeetingRooms(self):
        # intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
        # result = self.solution.minMeetingRooms(intervals)
        # self.assertEqual(result, 2)

        # intervals = [Interval(4, 9)]
        # result = self.solution.minMeetingRooms(intervals)
        # self.assertEqual(result, 1)

        intervals = [
            Interval(1, 5),
            Interval(5, 10),
            Interval(10, 15),
            Interval(15, 20),
            Interval(1, 20),
            Interval(2, 6),
        ]
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, 3)


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key=lambda interval: interval.start)
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        s = 0
        e = 0
        max_count = 0
        count = 0
        while s < len(starts):
            start = starts[s]
            end = ends[e]
            if start < end:
                count += 1
                max_count = max(max_count, count)
                s += 1
            else:
                count -= 1
                e += 1

        return max_count


if __name__ == "__main__":
    unittest.main()
