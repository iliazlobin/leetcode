import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_trap_water(self):
        heights1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected1 = 6
        self.assertEqual(
            self.solution.trap(heights1), expected1, f"Failed for input: {heights1}"
        )

        heights2 = [4, 2, 0, 3, 2, 5]
        expected2 = 9
        self.assertEqual(
            self.solution.trap(heights2), expected2, f"Failed for input: {heights2}"
        )


class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [], [0] * len(height)
        maxLeftHeight, maxRightHeight = 0, height[-1]
        for i in range(len(height)):
            maxLeftHeight = max(maxLeftHeight, height[i])
            maxLeft.append(maxLeftHeight)
            maxRightHeight = max(maxRightHeight, height[-i - 1])
            maxRight[-i - 1] = maxRightHeight
        water = 0
        for i in range(len(height)):
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            if diff > 0:
                water += diff
        return water


if __name__ == "__main__":
    unittest.main()
