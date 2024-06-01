import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxAreaOfIsland(self):
        grid = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result, 6)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        maxArea = 0

        def dfs(r, c):
            nonlocal maxArea

            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            area = 1 + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r, c + 1)
            maxArea = max(maxArea, area)
            return area

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)

        return maxArea


if __name__ == "__main__":
    unittest.main()
