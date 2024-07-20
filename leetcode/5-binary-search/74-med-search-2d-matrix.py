import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_searchMatrix(self):
        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 10
        self.assertTrue(self.solution.searchMatrix(matrix, target))

        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 15
        self.assertFalse(self.solution.searchMatrix(matrix, target))

        matrix = [[1, 1]]
        target = 2
        self.assertFalse(self.solution.searchMatrix(matrix, target))

        matrix = [[1], [3]]
        target = 3
        self.assertTrue(self.solution.searchMatrix(matrix, target))


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS = len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            # if target >= matrix[row][0] and target <= matrix[row][COLS]:
            if target < matrix[row][0]:
                bottom -= 1
            elif target > matrix[row][COLS]:
                top += 1
            else:
                break

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True

        return False


if __name__ == "__main__":
    unittest.main()
