import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxAreaOfIsland(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 6)

        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        def dfs(r, c, area):
            nonlocal maxArea

            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or (r, c) in visit
                or grid[r][c] == 0
            ):
                return 0

            # if area > 5:
            #     print(r, c, grid[r][c])
            # maxArea = max(maxArea, area)
            visit.add((r, c))
            return (
                1
                + dfs(r - 1, c, area + 1)
                + dfs(r, c - 1, area + 1)
                + dfs(r + 1, c, area + 1)
                + dfs(r, c + 1, area + 1)
            )

        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r, c, 0)
                maxArea = max(maxArea, area)

        return maxArea


if __name__ == "__main__":
    unittest.main()
