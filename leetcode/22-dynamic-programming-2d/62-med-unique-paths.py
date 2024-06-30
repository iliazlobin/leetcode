import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_uniquePaths(self):
        self.assertEqual(self.solution.uniquePaths(3, 7), 28, "Example 1 failed")
        self.assertEqual(self.solution.uniquePaths(3, 2), 3, "Example 2 failed")


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r + 1][c] == 0 and grid[r][c + 1] == 0:
                    grid[r][c] = 1
                else:
                    grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
        return grid[0][0]


if __name__ == "__main__":
    unittest.main()
