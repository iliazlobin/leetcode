import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_moveZeroes_example1(self):
        nums = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_moveZeroes_example2(self):
        nums = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_moveZeroes_custom(self):
        nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, [4, 2, 4, 3, 5, 1, 0, 0, 0, 0])


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            if nzums[l] != 0:
                l += 1
                if r < l:
                    r = l + 1
            elif nums[r] == 0:
                r += 1
            else:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r += 1


if __name__ == "__main__":
    unittest.main()
