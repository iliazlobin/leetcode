import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_dailyTemperatures(self):
        # Test case 1
        temperatures = [30, 38, 30, 36, 35, 40, 28]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, [1, 4, 1, 2, 1, 0, 0])

        # Test case 2
        temperatures = [22, 21, 20]
        result = self.solution.dailyTemperatures(temperatures)
        self.assertEqual(result, [0, 0, 0])


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for ti, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_index, stack_temp = stack.pop()
                res[stack_index] = ti - stack_index
            stack.append((ti, t))
        return res


if __name__ == "__main__":
    unittest.main()
