import unittest
from collections import Counter, deque
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rottingFruit(self):
        grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, 4)

        grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, -1)

        grid = [[0]]
        result = self.solution.orangesRotting(grid)
        self.assertEqual(result, 0)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh.add((r, c))

        def bfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append([r, c])
            fresh.remove((r, c))

        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                bfs(r - 1, c)
                bfs(r, c - 1)
                bfs(r + 1, c)
                bfs(r, c + 1)
            if q:
                time += 1

        return time if len(fresh) == 0 else -1


if __name__ == "__main__":
    unittest.main()
