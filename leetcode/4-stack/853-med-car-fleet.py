import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_car_fleet_example1(self):
        self.assertEqual(
            self.solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3
        )

    def test_car_fleet_example2(self):
        self.assertEqual(self.solution.carFleet(10, [3], [3]), 1)

    def test_car_fleet_example3(self):
        self.assertEqual(self.solution.carFleet(100, [0, 2, 4], [4, 2, 1]), 1)


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(key=lambda p: p[0], reverse=True)
        
        res = []
        for pos, speed in pairs:
            t = (target - pos) / speed
            if res and t <= res[-1]:
                continue
            res.append(t)
        
        return len(res)


if __name__ == "__main__":
    unittest.main()
