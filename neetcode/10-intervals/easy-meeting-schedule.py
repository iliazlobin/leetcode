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

    def test_canAttendMeetings(self):
        intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        result = self.solution.canAttendMeetings(intervals)
        self.assertFalse(result)

        intervals = [Interval(5, 8), Interval(9, 15)]
        result = self.solution.canAttendMeetings(intervals)
        self.assertTrue(result)

        intervals = [Interval(5, 10), Interval(0, 4)]
        result = self.solution.canAttendMeetings(intervals)
        self.assertTrue(result)


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        if len(intervals) == 0:
            return True
        prev_interval = intervals[0]
        for interval in intervals[1:]:
            if prev_interval.end > interval.start:
                return False
            prev_interval = interval
        return True


if __name__ == "__main__":
    unittest.main()
