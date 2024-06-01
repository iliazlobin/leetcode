import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def test_time_map(self):
        time_map = TimeMap()
        # time_map = OnTimeMap()
        time_map.set("alice", "happy", 1)
        self.assertEqual(time_map.get("alice", 1), "happy")
        self.assertEqual(time_map.get("alice", 2), "happy")
        time_map.set("alice", "sad", 3)
        self.assertEqual(time_map.get("alice", 3), "sad")

    def test_time_map_multiple_sets(self):
        time_map = TimeMap()
        # time_map = OnTimeMap()
        time_map.set("love", "high", 10)
        time_map.set("love", "low", 20)
        self.assertEqual(time_map.get("love", 5), "")
        self.assertEqual(time_map.get("love", 10), "high")
        self.assertEqual(time_map.get("love", 15), "high")
        self.assertEqual(time_map.get("love", 20), "low")
        self.assertEqual(time_map.get("love", 25), "low")


class OnTimeMap:  # doesn't pass leetcode heavy case
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        pairs = self.map[key]
        # pairs.sort(key=lambda p: p[1]) # always increasing order
        if timestamp < pairs[0][1]:
            return ""
        prev = pairs[0][0]
        for v, t in pairs[1:]:
            if timestamp < t:
                break
            prev = v
        return prev


class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value, timestamp))
        else:
            self.map[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        values = self.map.get(key, [])
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == "__main__":
    unittest.main()
