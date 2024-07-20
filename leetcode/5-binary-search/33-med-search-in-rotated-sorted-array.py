import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

        nums = [5, 1, 3]
        target = 5
        self.assertEqual(self.solution.search(nums, target), 0)

        nums = [5, 1, 3]
        target = 3
        self.assertEqual(
            self.solution.search(nums, target), 2, "Target 3 should be at index 2"
        )


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


if __name__ == "__main__":
    unittest.main()
