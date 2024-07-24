import unittest
from collections import Counter
from typing import List, Optional

from regex import F


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_example1(self):
    #     grid = [[2, 5, 4], [1, 5, 1]]
    #     expected_output = 4
    #     self.assertEqual(self.solution.gridGame(grid), expected_output)

    # def test_example2(self):
    #     grid = [[3, 3, 1], [8, 5, 2]]
    #     expected_output = 4
    #     self.assertEqual(self.solution.gridGame(grid), expected_output)

    # def test_example3(self):
    #     grid = [[1, 3, 1, 15], [1, 3, 3, 1]]
    #     expected_output = 7
    #     self.assertEqual(self.solution.gridGame(grid), expected_output)

    def test_custom_case(self):
        grid = [
            [20, 3, 20, 17, 2, 12, 15, 17, 4, 15],
            [20, 10, 13, 14, 15, 5, 2, 3, 14, 3],
        ]
        expected_output = 63
        self.assertEqual(self.solution.gridGame(grid), expected_output)


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        first, second = 0, 0

        for i in range(1, COLS):
            first += grid[0][i]
            second += grid[1][i - 1]

        res = first if first < second else second

        second = 0
        for i in range(1, COLS - 1):
            first -= grid[0][i]
            second += grid[1][i - 1]
            biggest = first if first > second else second
            res = min(res, biggest)

        return res


if __name__ == "__main__":
    unittest.main()
