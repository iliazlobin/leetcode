import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = NeetCodeSolution()

    def test_largestRectangleArea(self):
        heights = [7, 1, 7, 2, 2, 4]
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 8)

        heights = [1, 3, 7]
        result = self.solution.largestRectangleArea(heights)
        self.assertEqual(result, 7)


# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if len(heights) < 2:
#             return 0
#         max_area = 0
#         for lhi, lh in enumerate(heights):
#             for rhi, rh in enumerate(heights):
#                 if rhi <= lhi:
#                     continue
#                 min_h = lh if lh < rh else rh
#                 dist = rhi - lhi
#                 area = min_h * dist
#                 if area > max_area:
#                     max_area = area
#         return max_area


class NeetCodeSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


if __name__ == "__main__":
    unittest.main()
