import unittest
from collections import Counter, defaultdict
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_interchangeableRectangles_example1(self):
        rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]
        expected = 6
        result = self.solution.interchangeableRectangles(rectangles)
        self.assertEqual(
            expected, result, f"Failed on Example 1 with {result} != {expected}"
        )

    def test_interchangeableRectangles_example2(self):
        rectangles = [[4, 5], [7, 8]]
        expected = 0
        result = self.solution.interchangeableRectangles(rectangles)
        self.assertEqual(
            expected, result, f"Failed on Example 2 with {result} != {expected}"
        )


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = defaultdict(int)  # ratio(count)
        for r in rectangles:
            ratio = r[1] / r[0]
            count[ratio] += 1
        res = 0
        for c in count.values():
            res += self.combinations(c)
        return res

    def combinations(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        res = 1
        for c in range(3, n + 1):
            res += c - 1
        return res


if __name__ == "__main__":
    unittest.main()
