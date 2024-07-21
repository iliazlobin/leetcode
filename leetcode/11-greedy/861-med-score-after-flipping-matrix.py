import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_matrixScore_example1(self):
    #     grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    #     expected = 39
    #     result = self.solution.matrixScore(grid)
    #     self.assertEqual(
    #         expected, result, f"Failed on Example 1 with {result} != {expected}"
    #     )

    # def test_matrixScore_example2(self):
    #     grid = [[0]]
    #     expected = 1
    #     result = self.solution.matrixScore(grid)
    #     self.assertEqual(
    #         expected, result, f"Failed on Example 2 with {result} != {expected}"
    #     )

    def test_matrixScore_custom(self):
        grid = [[0, 1], [0, 1], [0, 1], [0, 0]]
        expected = 11
        result = self.solution.matrixScore(grid)
        self.assertEqual(
            expected, result, f"Failed on custom test with {result} != {expected}"
        )


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

        for c in range(COLS):
            count = 0
            for r in range(ROWS):
                if grid[r][c] == 1:
                    count += 1
            if count < ROWS / 2:
                for r in range(ROWS):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += 2 ** (COLS - c - 1)

        return res


if __name__ == "__main__":
    unittest.main()
