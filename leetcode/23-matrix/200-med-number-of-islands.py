import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numIslands(self):
        # grid1 = [
        #     ["1", "1", "1", "1", "0"],
        #     ["1", "1", "0", "1", "0"],
        #     ["1", "1", "0", "0", "0"],
        #     ["0", "0", "0", "0", "0"],
        # ]
        # self.assertEqual(self.solution.numIslands(grid1), 1)

        # grid2 = [
        #     ["1", "1", "0", "0", "0"],
        #     ["1", "1", "0", "0", "0"],
        #     ["0", "0", "1", "0", "0"],
        #     ["0", "0", "0", "1", "1"],
        # ]
        # self.assertEqual(self.solution.numIslands(grid2), 3)

        grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or (r, c) in visit
                or grid[r][c] != "1"
            ):
                return

            visit.add((r, c))
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)

        return islands


if __name__ == "__main__":
    unittest.main()
