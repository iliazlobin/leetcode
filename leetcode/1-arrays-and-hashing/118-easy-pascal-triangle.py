import math
import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        numRows = 5
        expected_output = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(self.solution.generate(numRows), expected_output)

    def test_example2(self):
        numRows = 1
        expected_output = [[1]]
        self.assertEqual(self.solution.generate(numRows), expected_output)

    def test_zero_rows(self):
        numRows = 0
        expected_output = []
        self.assertEqual(self.solution.generate(numRows), expected_output)

    def test_two_rows(self):
        numRows = 2
        expected_output = [[1], [1, 1]]
        self.assertEqual(self.solution.generate(numRows), expected_output)

    def test_three_rows(self):
        numRows = 3
        expected_output = [[1], [1, 1], [1, 2, 1]]
        self.assertEqual(self.solution.generate(numRows), expected_output)


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(2, numRows + 1):
            row = [0] * i
            row[0], row[i - 1] = 1, 1
            for j in range(1, i - 1):
                row[j] = res[i - 2][j - 1] + res[i - 2][j]
            res.append(row)
        return res


if __name__ == "__main__":
    unittest.main()
