import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_car_fleet(self):
        self.assertEqual(
            self.solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3
        )
        self.assertEqual(self.solution.carFleet(10, [3], [3]), 1)
        self.assertEqual(self.solution.carFleet(100, [0, 2, 4], [4, 2, 1]), 1)


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(key=lambda p: p[0], reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


if __name__ == "__main__":
    unittest.main()
