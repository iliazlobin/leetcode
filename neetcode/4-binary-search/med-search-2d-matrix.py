import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_searchMatrix(self):
        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 10
        result = self.solution.searchMatrix(matrix, target)
        self.assertTrue(result)

        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 15
        result = self.solution.searchMatrix(matrix, target)
        self.assertFalse(result)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search_list = [i for row in matrix for i in row]
        while True:
            half = search_list[0 : int(len(search_list) / 2)]
            if len(half) >= 1:
                if target == half[-1]:
                    return True
                if target < half[-1]:
                    search_list = half
                    continue
            rest = search_list[len(half) :]
            search_list = rest
            if len(search_list) == 1:
                if target == search_list[0]:
                    return True
                else:
                    return False


class NeetCodeSolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


if __name__ == "__main__":
    unittest.main()
