import unittest
from collections import Counter
from typing import List, Optional


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortArrayByParity_example1(self):
        nums = [3, 1, 2, 4]
        result = self.solution.sortArrayByParity(nums)
        self.assertTrue(result[:2] in [[2, 4], [4, 2]])
        self.assertTrue(result[2:] in [[3, 1], [1, 3]])

    def test_sortArrayByParity_example2(self):
        nums = [0]
        result = self.solution.sortArrayByParity(nums)
        self.assertEqual(result, [0])


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 != 0:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
        return nums


if __name__ == "__main__":
    unittest.main()
