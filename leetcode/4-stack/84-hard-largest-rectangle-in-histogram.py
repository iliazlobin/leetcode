import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largestRectangleArea(self):
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(self.solution.largestRectangleArea([2, 4]), 4)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                maxArea = max(maxArea, height * width)
                start = index
            stack.append((start, h))

        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, width * h)

        return maxArea


if __name__ == "__main__":
    unittest.main()
