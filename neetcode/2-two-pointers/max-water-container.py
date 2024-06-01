import unittest
from typing import List, Optional

from regex import R


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i, h in enumerate(heights):
            for ii, hh in enumerate(heights):
                if ii <= i:
                    continue
                distance = ii - i
                min_height = h if h <= hh else hh
                area = distance * min_height
                if area > max_area:
                    max_area = area
        return max_area

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_area(self):
        heights = [1,7,2,5,4,7,3,6]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 36)

        heights = [2,2,2]
        result = self.solution.maxArea(heights)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()
