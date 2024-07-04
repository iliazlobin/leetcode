import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMinArrowShots_examples(self):
        # Example 1
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        self.assertEqual(
            self.solution.findMinArrowShots(points), 2, "Failed for Example 1"
        )

        # Example 2
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        self.assertEqual(
            self.solution.findMinArrowShots(points), 4, "Failed for Example 2"
        )

        # Example 3
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual(
            self.solution.findMinArrowShots(points), 2, "Failed for Example 3"
        )

        points = [
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ]
        self.assertEqual(
            self.solution.findMinArrowShots(points), 2, "Failed for complex case"
        )

        points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
        self.assertEqual(self.solution.findMinArrowShots(points), 2, "Failed for overlapping intervals")


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points)

        for i in range(1, len(points)):
            if points[i][0] <= points[i - 1][1]:
                res -= 1
                # points[i] = [max(points[i][0], points[i - 1][0]), min(points[i][1], points[i - 1][1])]
                points[i] = [points[i][0], min(points[i][1], points[i - 1][1])]

        return res


if __name__ == "__main__":
    unittest.main()
