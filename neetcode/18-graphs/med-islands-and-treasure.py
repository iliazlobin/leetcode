import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_islandsAndTreasure(self):
        grid = [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(
            grid, [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        )

        grid = [[0, -1], [2147483647, 2147483647]]
        self.solution.islandsAndTreasure(grid)
        self.assertEqual(grid, [[0, -1], [1, 2]])


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        q = deque()

        def addPath(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or (r, c) in visit
                or grid[r][c] == -1
            ):
                return
            q.append([r, c])
            visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addPath(r - 1, c)
                addPath(r, c - 1)
                addPath(r + 1, c)
                addPath(r, c + 1)
            dist += 1


if __name__ == "__main__":
    unittest.main()
