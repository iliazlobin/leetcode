import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_searchInsert(self):
        self.assertEqual(
            self.solution.searchInsert([1, 3, 5, 6], 5),
            2,
            "Target 5 should be at index 2",
        )
        self.assertEqual(
            self.solution.searchInsert([1, 3, 5, 6], 2),
            1,
            "Target 2 should be inserted at index 1",
        )
        self.assertEqual(
            self.solution.searchInsert([1, 3, 5, 6], 7),
            4,
            "Target 7 should be inserted at index 4",
        )


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        return l


if __name__ == "__main__":
    unittest.main()
