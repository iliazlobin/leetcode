import heapq
import unittest
from collections import Counter
from typing import List, Optional

from torch import col_indices_copy


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_swimInWater(self):
        grid1 = [[0, 2], [1, 3]]
        self.assertEqual(self.solution.swimInWater(grid1), 3, "Example 1 failed")

        grid2 = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        self.assertEqual(self.solution.swimInWater(grid2), 16, "Example 2 failed")


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        visit.add((0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr == N or nc == N or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])


if __name__ == "__main__":
    unittest.main()
