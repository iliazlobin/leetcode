import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_setZeroes(self):
        # matrix = [[0, 1], [1, 1]]
        # self.solution.setZeroes(matrix)
        # self.assertEqual(matrix, [[0, 0], [0, 1]])

        # matrix = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
        # self.solution.setZeroes(matrix)
        # self.assertEqual(matrix, [[1, 0, 3], [0, 0, 0], [6, 0, 8]])

        # matrix = [[0,1]]
        # self.solution.setZeroes(matrix)
        # self.assertEqual(matrix, [[0,0]])

        matrix = [[1],[0]]
        self.solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0],[0]])

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

if __name__ == "__main__":
    unittest.main()
