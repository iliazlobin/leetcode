import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestIncreasingPath(self):
        matrix1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
        self.assertEqual(
            self.solution.longestIncreasingPath(matrix1), 4, "Example 1 failed"
        )
        matrix2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
        self.assertEqual(
            self.solution.longestIncreasingPath(matrix2), 4, "Example 2 failed"
        )
        matrix3 = [[1]]
        self.assertEqual(
            self.solution.longestIncreasingPath(matrix3), 1, "Example 3 failed"
        )


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}

        def dfs(r, c, val):
            if (
                r < 0
                or r >= len(matrix)
                or c < 0
                or c >= len(matrix[0])
                or matrix[r][c] <= val
            ):
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))

            cache[(r, c)] = res
            return res

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1)

        return max(cache.values())


if __name__ == "__main__":
    unittest.main()
