import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findPeakElement(self):
        self.assertEqual(
            self.solution.findPeakElement([1, 2, 3, 1]),
            2,
            "The peak element at index 2",
        )
        self.assertIn(
            self.solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]),
            [1, 5],
            "The peak element at index 1 or 5",
        )
        self.assertEqual(
            self.solution.findPeakElement([1, 2]),
            1,
            "The peak element at index 1",
        )


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m
        return l


if __name__ == "__main__":
    unittest.main()
