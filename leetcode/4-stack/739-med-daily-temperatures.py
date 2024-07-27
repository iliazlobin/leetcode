import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_daily_temperatures(self):
        self.assertEqual(
            self.solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertEqual(
            self.solution.dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0]
        )
        self.assertEqual(self.solution.dailyTemperatures([30, 60, 90]), [1, 1, 0])


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                inx, _ = stack.pop()
                res[inx] = i - inx

            stack.append((i, t))
        return res


if __name__ == "__main__":
    unittest.main()
