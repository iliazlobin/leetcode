import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_trap(self):
        height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(self.solution.trap(height1), 6, "Example 1 failed")

        height2 = [4, 2, 0, 3, 2, 5]
        self.assertEqual(self.solution.trap(height2), 9, "Example 2 failed")


class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = maxLeft.copy()
        leftHight = height[0]
        rightHight = height[-1]

        for i in range(len(height)):
            leftHight = max(leftHight, height[i])
            maxLeft[i] = leftHight
            rightHight = max(rightHight, height[-i - 1])
            maxRight[-i - 1] = rightHight

        water = 0
        for i in range(1, len(height) - 1):
            minHeight = min(maxLeft[i], maxRight[i])
            diff = minHeight - height[i]
            if diff > 0:
                water += diff
        
        return water

if __name__ == "__main__":
    unittest.main()
