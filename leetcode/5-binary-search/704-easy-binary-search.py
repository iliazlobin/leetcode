import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        self.assertEqual(self.solution.search(nums, target), 4)

        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        self.assertEqual(self.solution.search(nums, target), -1)

        nums = [5]
        target = 5
        self.assertEqual(self.solution.search(nums, target), 0)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


if __name__ == "__main__":
    unittest.main()
