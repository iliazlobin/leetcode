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

        matrix = [[1,1]]
        target = 2
        self.assertFalse(self.solution.searchMatrix(matrix, target))

        matrix = [[1],[3]]
        target = 3
        self.assertTrue(self.solution.searchMatrix(matrix, target))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        if len(matrix) > 1:
            while top <= bottom:
                row = (top + bottom) // 2
                if target > matrix[row][-1]:
                    top = row + 1
                elif target < matrix[row][0]:
                    bottom = row - 1
                else:
                    break
        else:
            row = 0
        first, last = 0, len(matrix[row]) - 1
        while first <= last:
            rm = (first + last) // 2
            if target < matrix[row][rm]:
                last = rm - 1
            elif target > matrix[row][rm]:
                first = rm + 1
            else:
                return True
        return False


if __name__ == "__main__":
    unittest.main()
