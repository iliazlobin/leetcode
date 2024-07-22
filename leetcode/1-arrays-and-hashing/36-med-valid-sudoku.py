import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValidSudoku(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertTrue(self.solution.isValidSudoku(board), "Example 1 failed")

        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertFalse(self.solution.isValidSudoku(board), "Example 2 failed")


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSets = [set() for _ in range(9)]
        rowSets = [set() for _ in range(9)]
        gridSets = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in rowSets[r]:
                        return False
                    rowSets[r].add(board[r][c])
                    if board[r][c] in colSets[c]:
                        return False
                    colSets[c].add(board[r][c])
                    if board[r][c] in gridSets[r // 3][c // 3]:
                        return False
                    gridSets[r // 3][c // 3].add(board[r][c])

        return True


if __name__ == "__main__":
    unittest.main()
