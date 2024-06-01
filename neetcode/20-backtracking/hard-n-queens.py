import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solveNQueens(self):
        n = 4
        result = self.solution.solveNQueens(n)
        self.assertEqual(
            sorted(result),
            sorted(
                [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
            ),
        )

        n = 1
        result = self.solution.solveNQueens(n)
        self.assertEqual(result, [["Q"]])


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or r - c in negDiag or r + c in posDiag:
                    continue
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                dfs(r + 1)
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        dfs(0)
        return res


if __name__ == "__main__":
    unittest.main()
