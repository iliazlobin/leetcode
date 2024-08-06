import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_totalNQueens_example1(self):
        n = 4
        expected_output = 2
        self.assertEqual(self.solution.totalNQueens(n), expected_output)

    def test_totalNQueens_example2(self):
        n = 1
        expected_output = 1
        self.assertEqual(self.solution.totalNQueens(n), expected_output)


class Solution(object):
    def totalNQueens(self, n):
        res = []
        cols = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for r in range(n)]

        def dfs(r):
            if r == n:
                line = ["".join(row) for row in board]
                res.append(line)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                cols.add((c))
                posDiag.add((r + c))
                negDiag.add((r - c))
                board[r][c] = "Q"
                dfs(r + 1)
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))

        dfs(0)
        return len(res)


if __name__ == "__main__":
    unittest.main()
