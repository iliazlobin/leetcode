import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMin(self):
        nums = [3, 4, 5, 6, 1, 2]
        result = self.solution.findMin(nums)
        self.assertEqual(result, 1)

        nums = [4, 5, 0, 1, 2, 3]
        result = self.solution.findMin(nums)
        self.assertEqual(result, 0)

        nums = [4, 5, 6, 7]
        result = self.solution.findMin(nums)
        self.assertEqual(result, 4)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        minimum = float("inf")

        while start < end:
            mid = start + (end - start) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

        return min(minimum, nums[start])


if __name__ == "__main__":
    unittest.main()

