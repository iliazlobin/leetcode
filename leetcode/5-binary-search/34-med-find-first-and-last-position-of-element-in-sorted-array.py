import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_searchRange(self):
        self.assertEqual(
            self.solution.searchRange([5, 7, 7, 8, 8, 10], 8),
            [3, 4],
            "Should be [3, 4]",
        )
        self.assertEqual(
            self.solution.searchRange([5, 7, 7, 8, 8, 10], 6),
            [-1, -1],
            "Should be [-1, -1]",
        )
        self.assertEqual(
            self.solution.searchRange([], 0), [-1, -1], "Should be [-1, -1]"
        )
        self.assertEqual(self.solution.searchRange([1], 1), [0, 0], "Should be [0, 0]")


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(leftBias):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                m = (l + r) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    i = m
                    if leftBias:
                        r = m - 1
                    else:
                        l = m + 1
            return i

        left = binSearch(True)
        right = binSearch(False)

        return [left, right]


if __name__ == "__main__":
    unittest.main()
